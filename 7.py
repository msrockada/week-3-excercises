import re
text = input()
x=re.search("[^a-z]+_",text)

if x:
    print("Not Matched")
else :
    print("Matched")