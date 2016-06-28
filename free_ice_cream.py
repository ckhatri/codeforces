# http://codeforces.com/problemset/problem/686/A

numInputs, numIcecream = map(int, raw_input().split(" "))
numDistressed = 0
for numInputs in xrange(0, numInputs):
	stringInput = map(str, raw_input().split(" "))
	sign = stringInput[0]
	amount = int(stringInput[1])
	if sign == "+":
		numIcecream += amount
	else:
		if amount > numIcecream:
			numDistressed += 1
		else:
			numIcecream -= amount
print "%d %d" % (numIcecream, numDistressed)

