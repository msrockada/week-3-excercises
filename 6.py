import re
text = input()
x=re.search("ab{2,3}",text)

if x:
    print("Matched")
else :
    print("Not Matched")