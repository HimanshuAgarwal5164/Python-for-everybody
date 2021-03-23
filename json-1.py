import json
data='''{
        "name":"Himanshu Agarwal",
        "phone":{
                "type":"intl",
                "number":"+91 9323388514"
                },
        "email":{
                "hide":"NO",
                "id":"himanshuagrawal5164@gmail.com"
                }
        }'''
info=json.loads(data)
print("Name is",info["name"])
print("Mobile number is",info["phone"]["number"])
if info["email"]["hide"].lower()=="no":
    print("E-Mail ID is",info["email"]["id"])
else:
    print("E-Mail ID is hidden")
