import re
text = input()
x=re.search("^\w",text)

if x:
    print("Matched")
else :
    print("Not Matched")