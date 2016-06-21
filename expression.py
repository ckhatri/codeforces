# http://codeforces.com/problemset/problem/479/A

def addOrMult(a, b):
	if a == 1 or b == 1:
		return a + b
	else:
		return a * b

a = int(input())
b = int(input())
c = int(input())

#can do op between a and b first, or b and c first.
d = addOrMult(a, b)
f = addOrMult(b, c)
result1 = addOrMult(c, d)
result3 = addOrMult(a, f)
if result1 >= result3:
	print result1
else:
	print result3
