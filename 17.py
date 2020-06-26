import re
text = input()
x=re.search("[0-9]",text)

if x:
    print("Matched")
else :
    print("Not Matched")