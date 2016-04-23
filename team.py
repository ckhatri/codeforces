# http://codeforces.com/problemset/problem/231/A
import sys

numWords = int(input())
numImplement = 0
for numWord in range(numWords):
	sureList = map(int, raw_input().split(" "))
	# if length > 10 print out abreviation which is simply first letter, num letters between, and last.
	count = 0
	for sure in sureList:
		count += sure
	if count > 1:
		numImplement += 1
print numImplement



