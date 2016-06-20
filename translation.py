# http://codeforces.com/problemset/problem/41/A
wordToTranslate = raw_input()
translatedWord = raw_input()

if wordToTranslate[::-1] == translatedWord:
	print "YES"
else:
	print "NO"