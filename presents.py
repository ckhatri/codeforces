# http://codeforces.com/problemset/problem/136/A

numFriends = input()
presentList = [-1] * numFriends
presentGivingList = map(int, raw_input().split(" "))
for pos in range(0, numFriends):
	gaveToPos = presentGivingList[pos]
	presentList[gaveToPos - 1] = pos + 1
for num in presentList:
	print num,
