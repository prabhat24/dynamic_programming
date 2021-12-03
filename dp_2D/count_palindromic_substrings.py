def count_palindromic_subsequence_bpdp(dp, arr, N):
	counter = 0
	for g in range(len(arr)):
		r = 0
		c = g
		while c<=N-1:
			if g == 0:
				dp[r][c] = True
				counter += 1
			elif g == 1 and arr[r] == arr[c]:
				dp[r][c] = True
				counter += 1
			elif g>1 and arr[r] == arr[c] and dp[r + 1][c - 1]:
				dp[r][c] = True
				counter += 1
			r +=1
			c +=1
	return counter 


if __name__ == '__main__':
	arr = "abaab"
	dp = [[False,] * len(arr) for k in range(len(arr))]
	res = count_palindromic_subsequence_bpdp(dp, arr, len(arr))
	print(res)
	print(res - len(arr))
