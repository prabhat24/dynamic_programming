
def iterative_cut_the_rod(dp, arr, N):
	for i in range(0, N):
		if i == 0:
			dp[i] = 0
			continue
		maxa = -1 
		for j in range(0, i):
			k = i - j
			maxa = max(dp[j] + arr[k], maxa)
		dp[i] = maxa
	print(dp)
	return dp[N-1]

if __name__ == '__main__':
	dp = []
	arr = [0, 1, 5, 8, 9, 10, 17, 17, 20]
	for i in arr:
		dp.append(-1)
	print(iterative_cut_the_rod(dp, arr, len(arr)))
