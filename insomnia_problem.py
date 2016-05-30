# http://codeforces.com/problemset/problem/148/A

# we know there are only four inputs
END_POS = 4
count = 0
listOfHits = []
notMultsList = []
for x in range(0, END_POS):
	listOfHits.append(int(input()))
numDragons = int(input())
# sort so that when we use a bool to break out of the inner loop, we always check with the smallest val first.
listOfHits.sort()
# for each dragon
for numDragon in range(1, numDragons+1):
	boolHit = False
	listPos = 0
	# get the divisor, then check if dragon num is divisble
	# short circuit if you've found divisble
	while not boolHit and listPos < END_POS:
		curDivisor = listOfHits[listPos]
		if numDragon % curDivisor == 0:
			count += 1
			boolHit = True
		listPos += 1
print count







