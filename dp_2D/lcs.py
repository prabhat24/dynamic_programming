# Longest Common Subsequence

def lcs_recursion1(str1, str2, st1, end1, st2, end2):
	# method1

	if end1 < st1 or end2 < st2:
		return 0

	if (st1<=end1 and st2<=end2) and str1[st1] == str2[st2]:
		c=  lcs_recursion(str1, str2, st1+1, end1, st2+1, end2) + 1
		print("one",c, st1, end1, st2, end2)
		return c
	else:
		a = lcs_recursion(str1, str2, st1, end1, st2+1, end2)
		b = lcs_recursion(str1, str2, st1+1, end1, st2, end2)
		c= max(a,b) 
		print("two",c, st1, end1, st2, end2)
		return c

def lcs_recursion2(str1, str2):
	# method1

	if len(str1) == 0 or len(str2) == 0:
		return 0

	if str1[0] == str2[0]:
		c=  lcs_recursion2(str1[1:], str2[1:]) + 1
		print("1", str1, str2, c)
		return c
	else:
		a = lcs_recursion2(str1[1:], str2)
		b = lcs_recursion2(str1, str2[1:])
		c= max(a,b)
		print("2", str1, str2, c)
		return c

def lcs_tddp(dp, str1, str2, st1, end1, st2, end2):
	# top down dp
	if end1 < st1 or end2 < st2:
		return 0
	print("here", st1, st2)
	if dp[st1][st2] != -1:
		return dp[st1][st2]		

	if (st1<=end1 and st2<=end2) and str1[st1] == str2[st2]:
		c = lcs_tddp(dp, str1, str2, st1+1, end1, st2+1, end2) + 1
		print("one", c, st1, end1, st2, end2)
		return c
	else:
		a = lcs_tddp(dp, str1, str2, st1, end1, st2+1, end2)
		b = lcs_tddp(dp, str1, str2, st1+1, end1, st2, end2)
		dp[st1][st2] = max(a,b) 
		print("two", dp[st1][st2], st1, end1, st2, end2)
		return dp[st1][st2]

if __name__ == '__main__':
	str1 = "abcde"
	str2 = "abc"
	dp = [[-1] * len(str2) for k in range(len(str1))]
	print(dp)
	c = lcs_tddp(dp, str1, str2, 0, len(str1) -1, 0, len(str2) -1)
	print(c)