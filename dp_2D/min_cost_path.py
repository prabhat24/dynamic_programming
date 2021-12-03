def recursion_min_cost(i, j, arr, rows, cols):
	if i == rows - 1 and j == cols - 1:
		return arr[i][j]
	if i == rows or j == cols:
		return 1<<32-1
	b, r, d = 1<<32-1,  1<<32-1,  1<<32-1
	if i < rows: 
		b = arr[i][j] + recursion_min_cost(i+1, j, arr, rows, cols)
	if j < cols:
		r = arr[i][j] + recursion_min_cost(i, j+1, arr, rows, cols)
	if i < rows and j < cols:
		d = arr[i][j] + recursion_min_cost(i+1, j+1, arr, rows, cols)
	ans = min(r, b, d)
	return ans


def iterative_min_cost(dp, arr, rows, cols):
	for i in range(rows-1, -1, -1):
		for j in range(cols-1, -1, -1):
			mina = 1 << 32 -1
			if i == rows -1 and j == 	cols -1:
				mina = 0
			if i + 1 < rows:
				mina = min(dp[i+1][j], mina)
			if j + 1 < cols:
				mina = min(dp[i][j+1], mina)
			if i + 1 < rows and j + 1 < cols:
				mina = min(dp[i+1][j+1], mina)
			dp[i][j] = mina + arr[i][j]
	return dp[0][0]


def top_down_min_cost(dp, i, j, arr, rows, cols):
	if i == rows - 1 and j == cols - 1:
		dp[i][j] = arr[i][j]
		return dp[i][j]
	if i == rows or j == cols:
		return 1<<32-1
	if dp[i][j] != -1:
		return dp[i][j]
	b, r, d = 1<<32-1, 1<<32-1,  1<<32-1
	if i < rows:
		b = arr[i][j] + top_down_min_cost(dp, i+1, j, arr, rows, cols)
	if j < cols:
		r = arr[i][j] + top_down_min_cost(dp, i, j+1, arr, rows, cols)
	if i < rows and j < cols:
		d = arr[i][j] + top_down_min_cost(dp, i+1, j+1, arr, rows, cols)

	ans = min(r, b, d)
	dp[i][j] = ans
	print(dp)
	return dp[i][j]
	


if __name__ == '__main__':
	cost= [[11, 2, 8, 6], [2, 12, 17, 6], [3, 3, 1, 8]]
	dp = []
	for i in range(0, len(cost)):
		a = [-1 for j in range(0, len(cost[0]))]
		dp.append(a)
	print(top_down_min_cost(dp, 0, 0,  cost, len(cost), len(cost[0])))