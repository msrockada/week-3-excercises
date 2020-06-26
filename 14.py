import re
text = input()
x=re.findall("[^a-zA-Z0-9_]",text)

if x:
    print("False")
else :
    print("True")