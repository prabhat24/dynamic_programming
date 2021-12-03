import copy

def max_price_recursion(arr):

	if len(arr) == 1:
		return arr[0]

	maxa = 0
	N = len(arr)
	for k in range(0, N):
		inc = 0
		if k == 0:
			inc = arr[k] * arr[k + 1]
		elif k == N-1:
			inc = arr[k-1] * arr[k]
		else:
			inc = arr[k-1] * arr[k] * arr[k+1]
		copy_arr = copy.deepcopy(arr)
		copy_arr.pop(k)
		each_ans = max_price_recursion(copy_arr) + inc
		maxa = max(maxa, each_ans)
	return maxa

def max_price_recursion2(arr, i, j):
	
	if i>j:
		return 0
	maxa = 0
	for k in range(i, j+1):
		inc = arr[k]
		if i-1 >= 0:
			inc = inc * arr[i-1]
		if j + 1 < len(arr):
			inc = inc * arr[j+1]
		ans = max_price_recursion2(arr, i, k-1) + max_price_recursion2(arr, k+1, j) + inc
		maxa = max(maxa, ans)
	return maxa


def max_price_dptd(dp, arr, i, j):
	if i>j:
		return 0
	if dp[i][j] != -1:
		return dp[i][j]
	maxa = 0
	for k in range(i, j+1):
		print(dp)
		inc = arr[k]
		if i-1 >= 0:
			inc = inc * arr[i-1]
		if j + 1 < len(arr):
			inc = inc * arr[j+1]
		ans = max_price_dptd(dp, arr, i, k-1) + max_price_dptd(dp, arr, k+1, j) + inc
		maxa = max(maxa, ans)
	dp[i][j] = maxa 
	return maxa

def get_val(dp, row, col):
	if row in range(len(dp)) and col in range(len(dp)):
		return dp[row][col]
	else:
		return 0

def bust_index(arr, j, N):
	inc = arr[j]
	if j >= 1:
		inc = inc * arr[j-1]
	if j <= N - 2:
		inc = inc * arr[j+1]
	return inc 

def get_bust_val(arr, k, st, end,  N):
	print("k--",k)
	inc = arr[k]
	if st-1 >= 0:
		inc = inc * arr[st-1]
	if end + 1 < len(arr):
		inc = inc * arr[end+1]
	return inc

def max_price_dpbp(dp, arr):
	N = len(arr)
	for g in range(N):
		if g == 0:
			for j in range(N):
				dp[j][j] = bust_index(arr, j, N)
		else:
			i = 0
			maxa = 0
			for j in range(g, N):
				print("j--", j)
				ptr_c = j - (g + 1)
				ptr_r = i + 1
				value = 0
				k = i
				while(ptr_c < j):	
					value = get_val(dp, i, ptr_c) + get_val(dp, ptr_r, j) + get_bust_val(arr, k, i, j, N)
					ptr_c +=1
					ptr_r +=1
					k += 1
					maxa = max(value, maxa)
				dp[i][j] = maxa
				i +=1
	print(dp)
	return dp[0][N-1]


if __name__ == '__main__':
	arr = [1,2,3,4]
	print(max_price_recursion(arr))
	print(max_price_recursion2(arr, 0, len(arr)-1))
	dp = [[0] * len(arr) for i in range(len(arr))]
	print(dp)
	# for k in arr:
	# 	dp.append(arr_dp)
	print(bust_index(arr, 0, len(arr)))
	print(max_price_dpbp(dp, arr))
	# print(max_price_dptd(dp, arr, 0, len(arr)-1))