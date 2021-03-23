import urllib.request,urllib.parse,urllib.error
import json

serviceurl="http://maps.googleapis.com/maps/api/geocode/json?"
address=input("Enter location")

url=serviceurl+urllib.parse.urlencode({'address':address})
print("Retrieving",url)

fhand=urllib.request.urlopen(url)
s=fhand.read()
data=s.decode()
print("Retrieving",len(data),"characters")
try:
    info=json.loads(data)
except:
    info=None

if not info or "status" not in info or info["status"]!="OK":
    print("\t\t\t------------Failed to Retrieve-----------------")
    print(data)
    exit()

lat=info["results"][0]["geometry"]["location"]["lat"]
long=info["results"][0]["geometry"]["location"]["lng"]
print("\nLatitude:\t",lat,"\nLongitude:\t",long)

loc=info["results"][0]["formatted_address"]
print(loc)
