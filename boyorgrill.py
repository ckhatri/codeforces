# http://codeforces.com/problemset/problem/236/A

input_str = raw_input()
usedLetters = []
countDistinct = 0
for char in input_str:
	if char not in usedLetters:
		usedLetters.append(char)
		countDistinct += 1
if countDistinct % 2 == 1:
	print "IGNORE HIM!"
else:
	print "CHAT WITH HER!"
