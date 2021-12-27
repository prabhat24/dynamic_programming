def max_val_recursion(cur, W, val_arr, wt_arr):
	if cur == len(val_arr):
		return 0
	else:
		inc, exc = 0,0
		if W-wt_arr[cur] >= 0:
			inc = val_arr[cur] + max_val(cur + 1, W - wt_arr[cur], val_arr, wt_arr)
		exc = max_val(cur + 1, W, val_arr, wt_arr)
		return max(inc, exc)

def max_val_top_down(dp, cur, W, val_arr, wt_arr):
	if cur == 0:
		dp[cur][W] = 0
		return dp[cur][W]
	elif W == 0:
		dp[cur][W] = 0
		return dp[cur][W]
	elif dp[cur][W] != -1:
		return dp[cur][W]
	else:
		inc, exc = 0,0
		if W-wt_arr[cur-1] >= 0:
			inc = val_arr[cur-1] + max_val_top_down(dp, cur - 1, W - wt_arr[cur-1], val_arr, wt_arr)
		exc = max_val_top_down(dp, cur - 1, W, val_arr, wt_arr)
		dp[cur][W] = max(inc, exc)
		return dp[cur][W]

def max_bottom_up(dp, W, val_arr, wt_arr):
	for i in range(0, len(val_arr) + 1):
		for j in range(0, W+1):
			if i == 0:
				dp[i][j] = 0
			if j == 0:
				dp[i][j] = 0
			else:
				inc, exc = 0, 0
				print("i", i)
				print("j", j)
				if j > wt_arr[i - 1]:
					inc = val_arr[i-1] + dp[i - 1][j-wt_arr[i-1]]
				exc = dp[i-1][j]
				dp[i][j] = max(exc, inc)
	return dp[len(val_arr)][W]


if __name__ == '__main__':
	val_arr = [15, 14, 10, 45, 30]
	wt_arr = [2, 5,1, 3, 4]
	W =7
	dp = []
	for i in range(0, len(val_arr)+1): 
		cols = [-1 for j in range(0, W+1)]
		dp.append(cols)
	print(max_val_top_down(dp, len(val_arr), W, val_arr, wt_arr))
