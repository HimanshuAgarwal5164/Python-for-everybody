import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
fhand=urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_480156.xml")
s=fhand.read()
data=s.decode()
tree=ET.fromstring(data)
l=tree.findall('comments/comment')
sum1=0
for x in l:
    s=x.find('count').text
    sum1=sum1+int(s)
print(sum1)
    
