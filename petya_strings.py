# http://codeforces.com/problemset/problem/112/A
firstWord = raw_input()
secondWord = raw_input()
firstWord = firstWord.lower()
secondWord = secondWord.lower()
if firstWord >secondWord:
	print 1
elif firstWord == secondWord:
	print 0
else:
	print -1