def max_value_recursion(i, j, wt_arr, v_arr):
	if j == 0:
		return 0
	if i < 0:
		return 0
	inc, exc = 0,0

	if j-wt_arr[i] >= 0:
		inc = max_value_recursion(i, j-wt_arr[i], wt_arr, v_arr) + v_arr[i]
	exc = max_value_recursion(i-1, j, wt_arr, v_arr)
	return max(inc, exc)



def max_value_bpdp(v_arr, wt_arr, capacity):
	dp = [0] * (capacity + 1)
	for r in range(0, len(wt_arr)):
		for i in range(len(dp)):
			if i == 0:
				dp[i] = 0
			elif i-wt_arr[r] >= 0:
				dp[i] = max(dp[i], dp[i-wt_arr[r]] + v_arr[r])
		print(dp)
	return dp[-1]


if __name__ == '__main__':
	wt_arr = [2, 5, 1, 3, 4]
	v_arr = [15, 14, 10, 45, 30]
	print(max_value_bpdp(v_arr, wt_arr, 7))

	print(max_value_recursion(4, 7, wt_arr, v_arr))

