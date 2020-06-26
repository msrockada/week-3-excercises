import re
text =" Python exercises, PHP exercises, C # exercises"
x= re.search("excercises",text)

print(x.span())