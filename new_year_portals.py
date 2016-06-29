# http://codeforces.com/problemset/problem/500/A

numCells, destNum = map(int, raw_input().split(" "))
portalsList = map(int, raw_input().split(" "))
currentPosition = 0
nonZeroPos = 1
while nonZeroPos < destNum:
	nextDestination = portalsList[currentPosition]
	nonZeroPos += nextDestination
	currentPosition = nonZeroPos - 1
if nonZeroPos == destNum:
	print "YES"
else:
	print "NO"
