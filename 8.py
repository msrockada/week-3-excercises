import re
text = input()
x=re.search("[A-Z]+[a-z]",text)

if x:
    print("Matched")
else :
    print("Not Matched")