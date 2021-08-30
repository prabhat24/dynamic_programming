def fib(n, dp):
	if n == 0 or n == 1:
		dp[n] = n
		return n
	if dp[n] != -1:
		return dp[n]
	else:
		dp[n] = fib(n-1, dp) + fib(n-2, dp)
		return dp[n]

if __name__ == "__main__":
	n = 10
	dp = list()
	for i in range(n+1):
		dp.append(-1)
	print(fib(n, dp))

