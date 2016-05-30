# http://codeforces.com/problemset/problem/263/A

currRowNum = 0
boolOneFound = False
oneRowPos = -1
oneColPos = -1
while not boolOneFound and currRowNum < 5:
	checkingRow = map(int, raw_input().split(" "))
	colPos = 0
	while not boolOneFound and colPos < 5:
		if checkingRow[colPos] == 1:
			boolOneFound = True
			oneRowPos = currRowNum
			oneColPos = colPos
		colPos += 1
	currRowNum += 1
middleRowPos = 2
middleColPos = 2
numMoves = 0
numMoves += abs(middleRowPos-oneRowPos)
numMoves += abs(middleColPos-oneColPos)
print numMoves



