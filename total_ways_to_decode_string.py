def ways_to_decode_string(arr, N):
	dp = [0] * N
	if arr and arr[0]:
		dp[0] = 1
	else:
		dp[0] = 0
	if N > 1:
		if arr[1] > 0 and arr[0] > 0: # non zero , non zero
			if int(str(arr[0]) + str(arr[1])) in range(1, 27):
				dp[1] = dp[0] + 1
			else:
				dp[1] = dp[0]
		elif arr[1] > 0 and arr[0] == 0: # zero , non zero
			dp[1] = 0
		elif arr[1] == 0 and arr[0] > 0: # non zero, zero 
			if int(str(arr[0]) + str(arr[1])) in range(1, 27):
				dp[1] = 1
			else:
				dp[1] = 0
		elif arr[1] == 0 and arr[0] == 0: # zero, zero
			dp[1] = 0
	for i in range(2, N):
		cnt1, cnt2 = 0, 0
		if arr[i] > 0 and arr[i-1] > 0: # non zero , non zero
			cnt1 = dp[i-1]
			if int(str(arr[i-1]) + str(arr[i])) in range(1, 27):
				cnt2 = dp[i-2]
		elif arr[i] > 0 and arr[i-1] == 0: # zero , non zero
			cnt1 = dp[i-1]
		elif arr[i] == 0 and arr[i-1] > 0: # non zero, zero 
			if int(str(arr[0]) + str(arr[1])) in range(1, 27):
				cnt2 = dp[i-2]
		dp[i] = cnt1 + cnt2
	print(dp)
	return dp[N-1]


if __name__ == '__main__':
	inp = str(input())
	arr = []
	print(arr)
	for char in inp:
		arr.append(int(char))
	print(arr)
	ans = ways_to_decode_string(arr, len(arr))
	print(ans)