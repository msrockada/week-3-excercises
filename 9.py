import re
text = input()
x=re.search("a*?b$",text)

if x:
    print("Matched")
else :
    print("Not Matched")