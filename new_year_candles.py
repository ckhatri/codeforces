# http://codeforces.com/problemset/problem/379/A

numCandles, reuseNum = map(int, raw_input().split(" "))
originalNumCandles = numCandles
countCandles = 0
remainderCandles = 1
while numCandles >= reuseNum:
	remainderCandles = numCandles % reuseNum
	numCandles /= reuseNum
	countCandles += numCandles
	numCandles += remainderCandles
print "%d" % (originalNumCandles + countCandles)
