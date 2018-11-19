import re
s = r'\d+'
pattern = re.compile(s)

m = pattern.search("one123adfnb52")
print(m.group())

m = pattern.search("one123adfnb52", 4, 15)
print(m.group())