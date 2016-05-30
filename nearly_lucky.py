# http://codeforces.com/problemset/problem/110/A

def isLucky(number):
	boolLucky = True
	lengthOfNumber = len(number)
	pos = 0
	while boolLucky and pos < lengthOfNumber:
		intDigit = int(number[pos])
		if not (intDigit == 4 or intDigit == 7):
			boolLucky = False
		pos += 1
	return boolLucky

def countLucky(number):
	count = 0
	for num in number:
		intDigit = int(num)
		if (intDigit == 4 or intDigit == 7):
			count += 1
	return count


def main():
	inputNum = raw_input()
	luckyNums = countLucky(inputNum)
	boolIsNearlyLucky = isLucky(str(luckyNums))
	if boolIsNearlyLucky:
		print "YES"
	else:
		print "NO"

main()
