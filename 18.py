import re
text = input()
x=re.findall("[0-9]{1,3}",text)

print (x)