try:
    print("url 1")
    from urllib.request import HTTPCookieProcessor, build_opener, install_opener, Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    print("get 3!")

import re
import time


course = input("Enter course number: ")
section = input("Enter section number: ")
year = input("Enter year: ")
department = input("Enter department(all caps): ")

totalSeats = re.compile("<td width=&#39;200px&#39;>Total Seats Remaining:</td><td align=&#39;left&#39;><strong>(.*?)</strong></td>")
generalSeats = re.compile("<td width=&#39;200px&#39;>General Seats Remaining:</td><td align=&#39;left&#39;><strong>(.*?)</strong></td>")
restrictedSeats = re.compile("<td width=&#39;200px&#39;>Restricted Seats Remaining\*:</td><td align=&#39;left&#39;><strong>(.*?)</strong></td>")

url = "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=" + department + "&course=" + course + "&section=" + section

print(url)

#get url
response = urlopen(url)
htmlText = response.read().decode("utf8")
total= re.search(totalSeats, htmlText)
general = re.search(generalSeats, htmlText)
restricted = re.search(restrictedSeats, htmlText)
print(total.group(1))
print(restricted.group(1))
print(general.group(1))
