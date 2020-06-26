import re
text = "Python exercises, PHP exercises, C# exercises"
x=re.search("exercises",text)

if x:
    print("Matched")
else :
    print("Not Matched")