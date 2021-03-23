import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

fhand=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_480154.html')
s=fhand.read()
s=s.decode()
soup=BeautifulSoup(s,'html.parser')
tags=soup('span')
sum1=0
for x in tags:
    a=x.contents[0]
    sum1=sum1+int(a)
print("Total sum=",sum1)
