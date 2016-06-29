# http://codeforces.com/problemset/problem/318/A

numNaturals, position = map(int, raw_input().split(" "))
numOdds = numNaturals / 2 + numNaturals % 2
valueOfPos = 0
if position <= numOdds:
	valueOfPos = 1 + 2*(position - 1)
else:
	valueOfPos = 2*(position - numOdds)
print valueOfPos