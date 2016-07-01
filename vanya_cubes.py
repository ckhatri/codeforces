# http://codeforces.com/problemset/problem/492/A

numBlocks = int(input())
count = 1
levelCount = 0
lastCount = 0
levelCount = 0
while numBlocks >= 0:
	numSubtract = count + lastCount
	numBlocks -= numSubtract
	lastCount = numSubtract
	count += 1
	levelCount += 1
print levelCount - 1