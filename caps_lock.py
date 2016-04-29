# http://codeforces.com/problemset/problem/131/A
word = raw_input()
if word.isupper():
	print word.lower()
elif (word[0].islower()):
	if word[1:].isupper() or word[1:] == "":
		print word[0].upper() + word[1:].lower()
	else:
		print word
else:
	print word
