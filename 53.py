import re
text = input()
x=re.sub("[a-z]","",text)

print(x)