import xml.etree.ElementTree as ET
data='''<stuff>
            <users>
                <user a='1'>
                    <name> Himanshu </name>
                    <id> 003 </id>
                </user>
                <user a='2'>
                    <name> Agarwal </name>
                    <id> 001</id>
                </user>
            </users>
        </stuff>'''
tree=ET.fromstring(data)
l=tree.findall('users/user')
for x in l:
    print("Person",x.get('a'))
    print("Name:",x.find('name').text)
    print("ID:",x.find('id').text)
    print("\n")
