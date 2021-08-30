def lis(arr, N, dp):
	if N == 1:
		dp[n-1] = 1
		return 1
	if dp[N-1] != -1:
		return dp[N-1]
	else:
		maxa = 1
		for i in range(1, N):
			each_ans = lis(arr, i, dp)
			if arr[N-1] > arr[i-1]:
				maxa = max(maxa, each_ans + 1) 
		dp[N-1] = maxa
		return maxa

if __name__ == "__main__":
	arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, 1]
	dp = []
	for _ in arr:
		dp.append(-1) 
	N = len(arr)
	lis(arr, N, dp)
	m = -1
	for i in dp:
		m = max(m, i)
	print(dp)