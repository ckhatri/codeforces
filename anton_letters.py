# http://codeforces.com/problemset/problem/443/A

letters = map(str, raw_input().strip("{}").split(", "))
if not letters[0] == "":
	setOfLetters = set(letters)
	print len(setOfLetters)
else:
	print "0"