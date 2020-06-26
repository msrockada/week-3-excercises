import re
text = input()
x=re.search("^1",text)

if x:
    print("Matched")
else :
    print("Not Matched")