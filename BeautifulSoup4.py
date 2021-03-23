import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url="http://py4e-data.dr-chuck.net/known_by_Benji.html"
for i in range(0,7):
    fhand=urllib.request.urlopen(url)
    s=fhand.read()
    s=s.decode()
    soup=BeautifulSoup(s,'html.parser')
    tags=soup('a')
    t=tags[17]
    url=t.get('href',None)
print(t.contents[0])
