# test222.py

import sys
print("welcome to", "python", sep="~", end="!", file=sys.stderr)

f = open("c:\\work\\test.txt","wt")
print("file write",file=f)
f.close()
