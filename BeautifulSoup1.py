import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
fhand=urllib.request.urlopen("http://dr-chuck.com/")
s=fhand.read()
s=s.decode()
soup=BeautifulSoup(s,'html.parser')
tags=soup('a')
for x in tags:
    print(x.get('href',None))
