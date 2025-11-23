from re import split

with open('FinalAssignment.md','r') as f : s = f.read()
print(len(split("\s+",s)))