# http://codeforces.com/problemset/problem/144/A

numSoldiers = int(input())
soldierHeights = map(int, raw_input().split(" "))
minPosition = 0
minHeight = 200
# want to find closet min to the end so <=
for x in xrange(0,len(soldierHeights)):
	height = soldierHeights[x]
	if height <= minHeight:
		minHeight = height
		minPosition = x
minHeight = soldierHeights.pop(minPosition)
soldierHeights.append(minHeight)
numSwappedForMin = len(soldierHeights) - minPosition - 1
maxPosition = 0
maxHeight = 0
# want to find closest max to beginning so >
for x in xrange(0,len(soldierHeights)):
	height = soldierHeights[x]
	if height > maxHeight:
		maxHeight = height
		maxPosition = x
numSwappedForMax = maxPosition
print numSwappedForMin + numSwappedForMax