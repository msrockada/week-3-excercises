import re
text = input()
x=re.search("a{1}b",text)

if x:
    print("Matched")
else :
    print("Not Matched")