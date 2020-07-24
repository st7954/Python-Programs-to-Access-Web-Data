import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address=input("Enter the location: ")
url = serviceurl + urllib.parse.urlencode({'address':address,'key':42})
print(url)
html= urllib.request.urlopen(url, context=ctx)
data=html.read()
print(data)
print("End")

js=json.loads(data)
print(js)
print("End")
print(json.dumps(js,indent=2))

for i in js['results']:
    if 'place_id' not in i:
        continue
    else:
        print(i['place_id'])
        break #since only once in the list from seeing the json script
