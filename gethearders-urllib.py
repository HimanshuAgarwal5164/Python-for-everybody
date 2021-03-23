import urllib.request,urllib.parse,urllib.error
fhand=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
s=fhand.read()
s=s.decode()
headers=dict(fhand.getheaders())
for x in headers:
    print(x,":\t",headers[x])
print(s)
