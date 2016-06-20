# http://codeforces.com/problemset/problem/451/A

numRowSticks, numColSticks = map(int, raw_input().split(" "))
numIntersections = numRowSticks * numColSticks
turnCount = 0
lowerVal = 0
if numRowSticks > numColSticks:
	lowerVal = numColSticks
else:
	lowerVal = numRowSticks
if lowerVal % 2 == 0:
	print "Malvika"
else:
	print "Akshat"