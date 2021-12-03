
def rod_cutting_problem_recursion(arr, l):
	if l == 0:
		return 0
	elif l == 1:
		return arr[0]
	maxa = 0
	for i in range(1, l+1):
		val = arr[i-1] + rod_cutting_problem_recursion(arr, l - i)
		maxa = max(val, maxa)
	return maxa

def rod_cutting_problem_tddp(dp, arr, l):
	if dp[l] != -1:
		return dp[l]
	maxa = 0
	for i in range(1, l+1):
		val = arr[i-1] + rod_cutting_problem_tddp(dp, arr, l - i)
		maxa = max(val, maxa)
	dp[l] = maxa
	return dp[l]


if __name__ == '__main__':
	arr = [1, 5, 8, 9, 10, 17, 17, 20]
	print(rod_cutting_problem_recursion(arr, len(arr)))
	# creating dp array
	dp = [-1] * (len(arr) + 1)
	# base cases of dp
	dp[0] = 0
	dp[1] = arr[0]
	print(rod_cutting_problem_tddp(dp, arr, len(arr)))