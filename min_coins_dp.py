def min_c(amount, given_coins, dp):
	print("start amount", amount)
	print("start  array", dp)
	if amount == 0:
		dp[0] = 0
		print("end amount", amount)
		print("end array", dp)
		return 0
	if dp[amount] != -1:
		return dp[amount]
	else:
		max_int = 1<<32 - 1
		for c in given_coins:
			if amount - c >= 0:
				smaller_step = min_c(amount - c, given_coins, dp) + 1
				max_int = min(smaller_step, max_int)
		dp[amount] = max_int
		print("end amount", amount)
		print("end array", dp)
		print("end ans", max_int)
		return max_int


if __name__ == "__main__":
	amount = 13
	given_coins = [1, 2, 5, 10, 50]
	dp = list()
	for i in range(amount + 1):
		dp.append(-1)
	print(min_c(amount, given_coins, dp))