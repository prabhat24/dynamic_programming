def min_cost_bst_recursion(arr, t_arr, st, end):
	if st == end:
		return t_arr[st] * 1
	if st > end:
		return 0
	mina = 1 << 32 - 1
	for k in range(st, end +1):
		cost_ittr = min_cost_bst_recursion(arr,t_arr, st, k-1) + min_cost_bst_recursion(arr, t_arr, k+1, end) + sum(t_arr[st:end+1])
		mina = min(mina, cost_ittr)
	return mina

def min_cost_bst_tddp(dp, arr, t_arr, st, end):
	if st == end:
		return t_arr[st] * 1
	if st > end:
		return 0
	if dp[st][st] != -1:
		return dp[st][end]
	mina = 1 << 32 - 1
	for k in range(st, end +1):
		cost_ittr = min_cost_bst_tddp(dp ,arr,t_arr, st, k-1) + min_cost_bst_tddp(dp, arr, t_arr, k+1, end) + sum(t_arr[st:end+1])
		mina = min(mina, cost_ittr)
	dp[st][end] = mina
	return mina

if __name__ == '__main__':
	arr = [1, 3, 4, 5, 6, 7, 8, 9, 11]
	t_arr = [3, 6, 4, 8, 7, 3, 7, 4, 7]
	dp = [[-1] * len(arr) for k in arr] 
	print(min_cost_bst_tddp(dp, arr, t_arr, 0, len(arr)-1))
	print(min_cost_bst_recursion(arr, t_arr, 0, len(arr)-1))
