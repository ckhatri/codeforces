# http://codeforces.com/problemset/problem/71/A
import sys

numWords = int(input())
for numWord in range(numWords):
	word = raw_input()
	length = len(word)
	# if length > 10 print out abreviation which is simply first letter, num letters between, and last.
	if length > 10:
		numAbrv = length - 2
		firstLetter = word[0]
		lastLetter = word[length-1]
		print "%s%d%s" % (firstLetter, numAbrv, lastLetter)
	else:
		print word


