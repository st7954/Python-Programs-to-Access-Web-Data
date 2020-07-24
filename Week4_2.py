url="http://py4e-data.dr-chuck.net/known_by_Baron.html"
n=1
while n<=7:
  import urllib.request, urllib.parse, urllib.error
  from bs4 import BeautifulSoup
  import ssl

  ctx = ssl.create_default_context()
  ctx.check_hostname = False
  ctx.verify_mode = ssl.CERT_NONE

  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')

  tags = soup('a')
  url=str(tags[17].get('href', None))
  n=n+1
len=len(url)
x=url[39:len]
lis=x.split('.')
print(lis[0])
