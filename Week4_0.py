import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all('span')
print (tags)
count=0
for tag in tags:
    x=str(tag)
    y=re.findall('[0-9]+',x)
    i=int(y[0])
    count=count+i
print(count)
