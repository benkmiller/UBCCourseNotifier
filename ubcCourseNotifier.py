try:
    print("url 1")
    from urllib.request import HTTPCookieProcessor, build_opener, install_opener, Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    print("get 3!")

import re
import time
import smtplib
import getpass

def sendEmail(emailAddress, p):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(emailAddress, p)

    msg = "YOUR MESSAGE!"
    server.sendmail(emailAddress, emailAddress, msg)
    server.quit()

#get url
def check(url):
    response = urlopen(url)
    htmlText = response.read().decode("utf8")

    #total= re.search(totalSeats, htmlText)
    general = re.search(generalSeats, htmlText)
    restricted = re.search(restrictedSeats, htmlText)

    #print ("Total Seats: ", total.group(1))
    print ("Restricted Seats: ", restricted.group(1))
    print ("General Seats: ", general.group(1))

    if general:
        if general.group(1) != '0':
            return 1
        else:
            return 0
    else:
        #quit here
        print("Something went wrong, maybe you put the wrong url in or lost internet connection, try restarting")
        return 0
    if restricted:
        if restricted.group(1) != '0':
            return 2
        else:
            return 0
    else:
        print("Something went wrong, maybe you put the wrong url in or lost internet connection, try restarting")
        return 0

course = input("Enter course number: ")
section = input("Enter section number: ")
year = input("Enter year: ")
department = input("Enter department(all caps): ")
emailAddress = input("Enter email address: ")
p = getpass.getpass()

totalSeats = re.compile("<td width=&#39;200px&#39;>Total Seats Remaining:</td><td align=&#39;left&#39;><strong>(.*?)</strong></td>")
generalSeats = re.compile("<td width=&#39;200px&#39;>General Seats Remaining:</td><td align=&#39;left&#39;><strong>(.*?)</strong></td>")
restrictedSeats = re.compile("<td width=&#39;200px&#39;>Restricted Seats Remaining\*:</td><td align=&#39;left&#39;><strong>(.*?)</strong></td>")

url = "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=" + department + "&course=" + course + "&section=" + section


while True:
    status = check(url)

    if status == 1:
        print("GENERAL SEAT AVAILABLE SENDING EMAIL")
        sendEmail(emailAddress, p)
        break
    if status == 2:
        print("RESTRICTED DO SOMEHTING")
        break
    else:
        time.sleep(10)
