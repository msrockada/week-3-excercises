import re
text = input()
x=re.search("\Bz\B",text)

if x:
    print("Matched")
else :
    print("Not Matched")