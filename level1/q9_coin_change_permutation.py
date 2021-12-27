


def coin_change_permutation_bpdp(dp, arr):
	dp[0] = 1

	for wt in range(1, len(dp)):
		for coin in arr:
			if coin <= wt:
				dp[wt] += dp[wt - coin]
	print(dp)
	return dp[-1]


if __name__ == '__main__':
	arr = [2, 3, 5]
	arr.insert(0, 0)

	weight = 10
	dp = [0] * (weight + 1)
	print(coin_change_permutation_bpdp(dp, arr))