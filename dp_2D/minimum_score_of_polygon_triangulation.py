
def min_score_polygon_recursion(arr, i, j):
	if j - i <= 1:
		return 0
	else:
		mina = 1<<32 -1	
		for k in range(i+1, j):
			a = min_score_polygon_recursion(arr, i, k)
			b = arr[i] * arr[k] * arr[j]
			c = min_score_polygon_recursion(arr, k, j)
			value = a + b + c
			mina = min(mina, value)
		return mina

def min_score_polygon_tddp(dp, arr, i, j):
	if j - i <= 1:
		return 0
	if dp[i][j] != -1:
		return dp[i][j]
	else:
		mina = 1<<32 -1	
		for k in range(i+1, j):
			a = min_score_polygon_tddp(dp, arr, i, k)
			b = arr[i] * arr[k] * arr[j]
			c = min_score_polygon_tddp(dp, arr, k, j)
			value = a + b + c
			mina = min(mina, value)
		dp[i][j] =mina
		return dp[i][j]

if __name__ == '__main__':
	arr = [1,3,1,4,1,5]
	print(min_score_polygon_recursion(arr, 0, len(arr)-1))
	dp = [[-1] * len(arr) for _ in arr]
	print(min_score_polygon_tddp(dp, arr, 0, len(arr)-1))
	print(dp)