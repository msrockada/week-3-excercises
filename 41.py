import re
text = input()
x=re.sub("[a-zA-Z0-9]","",text)

print(x)