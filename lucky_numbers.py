# http://codeforces.com/problemset/problem/122/A
strNum = raw_input()
intNum = int(strNum)
# all luck numbers less than 1000, as given in program restriction
luckyList = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
luckyBoolFound = False
pos = 0
while not luckyBoolFound and pos < len(luckyList):
	luckyNum = luckyList[pos]
	if intNum % luckyNum == 0:
		luckyBoolFound = True
	pos += 1
if luckyBoolFound:
	print "YES"
else:
	print "NO"
