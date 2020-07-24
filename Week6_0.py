import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read().decode()
print (html)

print("End Segment")
stuff=json.loads(html)
print(stuff)
print("End Segment")
print(json.dumps(stuff,indent=4))# same thing prints as html prints with decode

print("End Segment")
sum=0
for i in stuff['comments']:
    sum=sum+int(i['count'])
print(sum)
