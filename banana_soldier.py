# http://codeforces.com/problemset/problem/546/A

initCost, initMoney, numBananas = map(int, raw_input().split(" "))
totalCost = 0
for x in range(1, numBananas+1):
	totalCost += initCost * x
if totalCost <= initMoney:
	print 0
else:
	print totalCost - initMoney