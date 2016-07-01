# http://codeforces.com/problemset/problem/61/A

firstInput = raw_input()
secondInput = raw_input()
result = ""
for pos in range(0, len(firstInput)):
	firstChar = firstInput[pos]
	secondChar = secondInput[pos]
	if firstChar == secondChar:
		result += "0"
	else:
		result += "1"
print result