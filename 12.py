import re
text = input()
x=re.findall("z",text)

if x:
    print("Matched")
else :
    print("Not Matched")