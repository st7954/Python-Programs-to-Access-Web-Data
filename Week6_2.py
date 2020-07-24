import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address=input("Enter the location: ")
parms = dict()
parms['address'] = address
if api_key is not False:
   parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print(url)
html= urllib.request.urlopen(url, context=ctx)
data=html.read().decode()

js=json.loads(data)
print(json.dumps(js,indent=2))

for i in js['results']:
    if 'place_id' not in i:
        continue
    else:
        print(i['place_id'])
