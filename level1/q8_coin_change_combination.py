def coin_change_combinations_bpdp(dp, arr, weight):
	for num in arr:
		for k in range(num, len(dp)):
			if k == 0:
				dp[k] = 1
			elif num == 0:
				dp[k] = 0
			elif k-num >= 0:
				dp[k] = dp[k] + dp[k-num]
	return dp[weight]



def coin_change_combinations_recursion(r, wt, arr):
	if wt == 0:
		return 1
	if wt <= 0:
		return 0
	elif r == 0:
		return 0
	return 	coin_change_combinations_recursion(r-1, wt, arr) + coin_change_combinations_recursion(r, wt-arr[r], arr)


if __name__ == '__main__':
	arr = [2, 3, 5]
	arr.insert(0, 0)
	print(coin_change_combinations_recursion(len(arr) -1, 7, arr))

	weight = 7
	dp = [0] * (weight+1)
	print(coin_change_combinations_bpdp(dp, arr, weight))