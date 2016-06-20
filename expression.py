def addOrMult(a, b):
	if a == 1 or b == 1:
		return a + b
	else:
		return a * b

a = int(input())
b = int(input())
c = int(input())

d = addOrMult(a, b)
result = addOrMult(c, d)
print result