# http://codeforces.com/problemset/problem/486/A

n = int(input())
result = n / 2 + n % 2
if n % 2 != 0:
	result *= -1
print result