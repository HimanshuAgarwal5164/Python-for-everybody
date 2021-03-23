import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

fhand=urllib.request.urlopen("https://en.wikipedia.org/wiki/Sachin_Tendulkar",context=ctx)
s=fhand.read()
s=s.decode()
soup=BeautifulSoup(s,'html.parser')
tags=soup('a')
for x in tags:
    print(x.get('href',None))
