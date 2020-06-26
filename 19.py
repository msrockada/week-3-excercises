import re
text = "The quick brown fox jumps over the lazy dog"
x=re.search("fox",text)
y = re.search ("dog",text)
z = re.search("horse",text)


if x:
    print("True")
else:
    print("False")

if y:
 print("True")
else:
  print("False")
if z:
 print("True")
else:
    print("False")