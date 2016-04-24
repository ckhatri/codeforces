# http://codeforces.com/problemset/problem/282/A

numOps = int(input())
count = 0
for op in range(numOps):
	operation = raw_input()
	if "+" in operation:
		count += 1
	elif "-" in operation:
		count -= 1
print count