# http://codeforces.com/problemset/problem/160/A

#finds the sum of the rest of coins in the list
def sumOfRest(coinsList):
	sumOfCoins = 0
	for num in coinsList:
		sumOfCoins += num
	return sumOfCoins

numCoins = int(input())
listOfCoins = map(int, raw_input().split(" "))
listOfCoins.sort(reverse=True) #sort in descending order so you can just go through and add all the big coins first.
myCoinsSum = 0
myCoinsCount = 0
coin = 0
finished = False 
# while the list isn't empty (you're popping) and sum of rest of coins isn't less than your count.
while len(listOfCoins) != 0 and not finished:
	# pop the largest val in the list, add it to your sum, add one to your count
	coin = listOfCoins.pop(0)
	myCoinsSum += coin
	myCoinsCount += 1
	# check to see if the sum of the rest of coins in list are less than yours, if you are then you're done.
	if sumOfRest(listOfCoins) < myCoinsSum:
		finished = True
		print myCoinsCount
