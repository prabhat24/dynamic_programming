# longest palindromic subsequence
def lps_recursion(str1 , st, end):
	if st == end:
		return 1
	elif st > end:
		return 0
	if str1[st] == str1[end]:
		return lps_recursion(str1, st+1, end-1) + 2 
	else:
		a = lps_recursion(str1, st, end-1)
		b = lps_recursion(str1, st+1, end)
		c = max(a,b)
		return c

def lps_tddp(dp, str1 , st, end):
	# dp solution
	if st > end:
		return 0
	elif st == end:
		dp[st][end] = 1
		return dp[st][end]
	if dp[st][end] != -1:
		return dp[st][end]
	if str1[st] == str1[end]:
		ans = lps_tddp(dp, str1, st+1, end-1) + 2
	else:
		a = lps_tddp(dp, str1, st, end-1)
		b = lps_tddp(dp, str1, st+1, end)
		ans = max(a,b)
	dp[st][end] = ans
	return dp[st][end]

if __name__ == '__main__':
	str1 = 'vcabbakd'
	dp = [[-1] * len(str1) for k in range(len(str1))]
	ans = lps_tddp(dp, str1, 0, len(str1)-1)
	print(dp)
	print(ans)
