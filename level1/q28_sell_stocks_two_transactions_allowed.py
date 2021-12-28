import sys
import math


def twoTransactions(arr, n):
	lol = [0] * n
	hol = [0] * n 
	# compute lol
	mina = 1<<32 - 1
	max_profit_upto_k = 0
	for k in range(0, n):
		mina = min(mina, arr[k])
		profit_at_k = arr[k] - mina
		max_profit_upto_k = max(profit_at_k, max_profit_upto_k)
		lol[k] = max_profit_upto_k

	maxa = 0
	global_max = 0
	max_profit_beyond_k = 0
	# compute hol
	# & compute global max
	for k in range(n-1, -1, -1):
		maxa = max(maxa, arr[k])
		profit_at_k = maxa - arr[k]
		max_profit_beyond_k = max(profit_at_k, max_profit_beyond_k)
		hol[k] = max_profit_beyond_k
		global_max = max(hol[k]+lol[k], global_max)
	print(global_max)
		
def main():
	n = int(input())
	array = []
	for i in range(n) :
		array.append(int(input()))
	twoTransactions(array, n)


if __name__ == '__main__':
	main()