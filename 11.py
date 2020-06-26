import re
text = input()
x=re.search("\w*?\S$",text)

if x:
    print("Matched")
else :
    print("Not Matched")