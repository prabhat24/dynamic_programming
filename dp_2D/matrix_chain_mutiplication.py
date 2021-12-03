# dynamic programming matrix chain multiplication

# mcm recursion will runturn minimum operation to multiply matrices represented from i to j
def mcm_recursion(dp, arr, i, j):
	ans = None
	if dp[i][j] != -1:
		return dp[i][j]
	if j-i<=1:
		dp[i][j] = 0
		ans = dp[i][j]
	else:
		mina = 1<<32 -1
		for k in range(i+1, j):
			each_ans = mcm_recursion(dp ,arr, i, k) + mcm_recursion(dp, arr, k, j) + arr[i] * arr[k] * arr[j]
			mina = min(mina, each_ans)
		ans = mina
		dp[i][j] = mina
	print("here it is", dp)
	return ans

if __name__ == '__main__':
	arr = [1,2,3,4,5]
	dp = []
	for _ in range(len(arr)):
		ar_dp = [-1] * (len(arr))
		dp.append(ar_dp)
	a = mcm_recursion(dp, arr, 0, len(arr)-1)
	print(a)
