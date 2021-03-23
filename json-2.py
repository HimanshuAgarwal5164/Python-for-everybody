import json
data='''[
            {   "name":"Himanshu Agarwal",
                "age":"21",
                "sex":"Male"
            },
            {   "name":"Shrawan Agarwal",
                "age":"48",
                "sex":"Male"
            },
            {   "name":"Seema Agarwal",
                "age":"47",
                "sex":"Female"
            }
        ]'''
info=json.loads(data)
i=1
for x in info:
    print("Person",i)
    i=i+1
    print("Name:\t",x['name'])
    print("Age:\t",x['age'])
    print("Sex:\t",x['sex'])
    print("\n")
