def boolean_parenthesization_recursion(t_dp, f_dp, arr, str2, i, j, N):
	if t_dp[i][j] != -1 and f_dp[i][j] != -1:
		return t_dp[i][j], f_dp[i][j]
	if i == j:
		if arr[i] == 'T':
			t_dp[i][j] = 1
			f_dp[i][j] = 0
		elif arr[i] == 'F':
			t_dp[i][j] = 0
			f_dp[i][j] = 1
		return t_dp[i][j], f_dp[i][j]

	if j - i == 1:
		operand1 = True if arr[i] == 'T' else False
		operand2 = True if arr[j] == 'T' else False
		if str2[i] == '^':
			ans = operand1 ^ operand2
		elif str2[i] == '&':
			ans = operand1 and operand2
		elif str2[i] == '|':
			ans = operand1 or operand2
		t_dp[i][j] = 1 if ans else 0
		f_dp[i][j] = 1 if not ans else 0
		return t_dp[i][j], f_dp[i][j]
	try:
		total_t_ways, total_f_ways = 0, 0
	 	for k in range(i, j):
	 		t_ways, f_ways = 0, 0
	 		ltw, lfw = boolean_parenthesization_recursion(t_dp, f_dp, arr, str2, i, k, N)
	 		rtw, rfw = boolean_parenthesization_recursion(t_dp, f_dp, arr, str2, k+1, j, N)
			if str2[k] == '|':
				t_ways = ltw * rtw + ltw * rfw + lfw * rtw
				f_ways = lfw * rfw
			elif str2[k] == '^':
				t_ways = ltw * rfw + lfw * rtw
				f_ways = lfw * rfw + ltw * rtw
			elif str2[k] == '&':
				t_ways = ltw * rtw
				f_ways =  ltw * rfw + lfw * rtw + lfw * rfw
			total_t_ways += t_ways
			total_f_ways += f_ways
		t_dp[i][j], f_dp[i][j] = total_t_ways, total_f_ways
	except Exception as e:
		print("exception occured" , i, j, k)
	return t_dp[i][j], f_dp[i][j]

if __name__ == '__main__':
	str1 = 'TTFT'
	str2 = '|&^'
	t_dp = [ [-1] * len(str1) for i in range(len(str1))]
	f_dp = [ [-1] * len(str1) for i in range(len(str1))]
	print(boolean_parenthesization_recursion(t_dp, f_dp, str1, str2, 0, len(str1) -1, len(str1)))
