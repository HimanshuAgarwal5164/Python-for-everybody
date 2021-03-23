import xml.etree.ElementTree as ET
data='''<person>
            <name> Himanshu Agarwal </name>
            <phone type='intl'> +91 93233 88514 </phone>
            <email hide='yes' />
        </person>'''
tree=ET.fromstring(data)
print("Name:",tree.find('name').text)
print("Email attribute says",tree.find('email').get('hide'))
print("Mobile number:",tree.find('phone').text)
