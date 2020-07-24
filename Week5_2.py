import urllib.request,urllib.parse,urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
tree=ET.fromstring(html)
lis=tree.findall('comments/comment')
print (lis)
sum=0
for i in lis:
    s=int(i.find('count').text)
    sum=sum+s
print(sum)
