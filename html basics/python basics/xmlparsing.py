import xml.etree.ElementTree as ET
mytree= ET.parse('Sample.xml')
myroot=mytree.getroot()
print(myroot.tag)
print(myroot[0].attrib)
for x in myroot[0]:
    print(x.tag,x.attrib)
for x in myroot[0]:
    print(x.text)
for x in myroot.findall('food'):# loop through food tag
    item=x.find('item').text
    price=x.find('price').text
    print(item,price)
for x in myroot.iter('description'):
    a=str(x.text)+'Description has been added'
    x.text=str(a)
    x.set('updated','yes')
mytree.write('new.xml')

ET.subElement(myroot[0],'speciality')
for x in myroot.iter('speciality'):
    b='South Indian Special'
    x.text=str(b)
mytree.write('new2.xml')
