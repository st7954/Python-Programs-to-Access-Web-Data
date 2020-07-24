import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

stuff=json.loads(html)

sum=0
for i in stuff['comments']:
    sum=sum+int(i['count'])
print(sum)
