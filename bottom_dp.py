def fib_bp(n, dp):
	dp[0] = 0
	dp[1] = 1

	for i in range(2, n + 1):
		dp[i] = dp[i - 1] + dp[i - 2]

	return dp[n]

def fib_2_vars(n):
	ptr1 = 0
	ptr2 = 1
	for i in range(2, n + 1):
		c = ptr1 + ptr2
		ptr1 = ptr2
		ptr2 = c
	return c

if __name__ == "__main__":
	n = 10
	dp = list()
	for _ in range(n + 1):
		dp.append(-1)
	print(fib_bp(n, dp))