# http://codeforces.com/problemset/problem/271/A

def isDistinct(yearInput):
	for firstDigit in yearInput:
		count = 0
		for secondDigit in yearInput:
			if secondDigit == firstDigit:
				count += 1
			if count > 1:
				return False
	return True

yearInput = raw_input()
notFound = True
intYear = int(yearInput)
while notFound:
	intYear += 1
	stringYear = str(intYear)
	if isDistinct(stringYear):
		notFound = False
print intYear
