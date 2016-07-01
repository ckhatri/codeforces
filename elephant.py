# http://codeforces.com/problemset/problem/617/A

distance = int(input())
numSteps = distance / 5
if not distance % 5 == 0:
	numSteps += 1
print numSteps
