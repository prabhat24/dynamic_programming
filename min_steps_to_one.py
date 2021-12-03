
# top down dp
def min_steps_to_one_tddp(dp, N):
	a,b,c = 1<<32-1, 1<<32-1, 1<32-1
	if dp[N] != -1:
		return dp[N]
	if N==1:
		dp[1] = 0
		return dp[1]
	if N%2 == 0:
		a = min_steps_to_one_tddp(N//2)
	if N%3 == 0:
		b = min_steps_to_one_tddp(N//3)
	c = min_steps_to_one_tddp(N-1)
	dp[N] = min(a,b,c) + 1 
	return dp[N]


# bottom up dp(itterative)
def min_steps_to_one_bpdp(dp, N):
	dp[1] = 0
	for num in range(2, N+1):
		a,b,c = 1<<32-1, 1<<32-1, 1<32-1
		if num % 2 == 0:
			a = dp[num/2]
		if num % 3 == 0:
			b = dp[num/3]
		c = dp[num-1]
		dp[num] = min(a,b,c) + 1
	return dp[N]


# recursion
def min_steps_to_one_recursion(N):
	a,b,c = 1<<32-1, 1<<32-1, 1<32-1
	if N==1:
		return 0
	if N%2 == 0:
		a = min_steps_to_one_recursion(N//2)
	if N%3 == 0:
		b = min_steps_to_one_recursion(N//3)
	c = min_steps_to_one_recursion(N-1)
	return min(a,b,c) + 1


if __name__ == '__main__':
	N = 10
	dp = [-1] * (N + 1)
	print(min_steps_to_one_recursion(N))
	print(min_steps_to_one_bpdp(dp, N))
	print(min_steps_to_one_tddp(dp, N))

