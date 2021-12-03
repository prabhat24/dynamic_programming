# Count Distinct Palindromic Subsequences

def dps_recursion(arr, st, end, N, nex, prev):
	if st > end:
		return 0
	if st==end:
		return 1

	if arr[st] == arr[end]:
		if nex[st] == prev[end]:
			return 2 * dps_recursion(arr, st+1, end-1, N, nex, prev) + 1
		elif nex[st] == end and st == prev[end]:
			return 2 * dps_recursion(arr, st+1, end-1, N, nex, prev) + 2
		else:
			l = nex[st]
			r = prev[end]
			return 2 * dps_recursion(arr, st+1, end-1, N, nex, prev) - dps_recursion(arr, l+1, r-1, N, nex, prev)

	
	else:
		return dps_recursion(arr, st, end-1, N, nex, prev) +  dps_recursion(arr, st+1, end, N, nex, prev) - dps_recursion(arr, st+1, end-1, N, nex, prev)


def dps_tddp(dp, arr, st, end, N, nex, prev):
	if st > end:
		return 0
	if st == end:
		dp[st][end] = 1
		return dp[st][end]

	if dp[st][end] != -1:
		return dp[st][end]

	if arr[st] == arr[end]:
		if nex[st] == prev[end]:
			ans =  2 * dps_tddp(dp, arr, st+1, end-1, N, nex, prev) + 1
		elif nex[st] == end and st == prev[end]:
			ans = 2 * dps_tddp(dp, arr, st+1, end-1, N, nex, prev) + 2
		else:
			l = nex[st]
			r = prev[end]
			ans = 2 * dps_tddp(dp, arr, st+1, end-1, N, nex, prev) - dps_tddp(dp, arr, l+1, r-1, N, nex, prev)

	
	else:
		ans = dps_tddp(dp, arr, st, end-1, N, nex, prev) +  dps_tddp(dp, arr, st+1, end, N, nex, prev) - dps_tddp(dp, arr, st+1, end-1, N, nex, prev)
	dp[st][end] = ans
	return dp[st][end]



if __name__ == '__main__':
	arr = "bccb"
	#"ayaxaya"
	N = len(arr)
	nex = [-1] * N
	prev = [-1] * N
	for i in range(N):
		for j in range(i+1, N):
			if arr[i] == arr[j]:
				nex[i] = j
				break
	for i in range(N-1, -1, -1):
		for j in range(i-1, -1, -1):
			if arr[i] == arr[j]:
				prev[i] = j
				break
	dp = [[-1] * N for k in range(N)]
	print(dps_tddp(dp, arr, 0, N-1, N, nex, prev))
