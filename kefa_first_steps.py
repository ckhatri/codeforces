# http://codeforces.com/problemset/problem/580/A

numNumbers = int(input())
count = 0
numbers = map(int, raw_input().split(" "))
prevNumber = numbers[0]
maxNonDescending = 1
for number in numbers:
	if number >= prevNumber:
		count += 1
		if count > maxNonDescending:
			maxNonDescending = count
	else:
		count = 1
	prevNumber = number
print maxNonDescending
