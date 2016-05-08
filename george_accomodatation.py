# http://codeforces.com/problemset/problem/467/A

numRooms = int(input())
count = 0
for roomNum in range(numRooms):
	numLiving, capacity = map(int, raw_input().split(" "))
	if numLiving + 2 <= capacity:
		count += 1
print count
