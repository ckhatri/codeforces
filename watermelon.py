# http://codeforces.com/problemset/problem/4/A

weight = int(input())
# if even and greater than 2 return true.
# special case if 2 because you can't split 2 evenly
if weight % 2 == 0 and weight > 2:
	print "YES"
else:
	print "NO"