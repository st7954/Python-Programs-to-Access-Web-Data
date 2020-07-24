import re
x="My name isa "
y=re.findall('\S+',x)
print(y)
