import re
lis=list()
name=input("Enter the file name ")
fhand=open(name)
for i in fhand:
    i=i.rstrip()
    if(len(i)<1):
      continue
    else:
      x=re.findall('[0-9]+',i)
      for j in x:
         j=int(j)
         lis.append(j)
print(sum(lis))
