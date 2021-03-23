import urllib.request,urllib.parse,urllib.error
import json
fhand=urllib.request.urlopen(" http://py4e-data.dr-chuck.net/comments_480157.json")
s=fhand.read()
data=s.decode()
info=json.loads(data)
sum1=0
a=info["comments"]
for x in a:
    s=x["count"]
    sum1=sum1+int(s)
print(sum1)
    
