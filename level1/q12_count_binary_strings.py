
def count_binary_strings_recursion(vacent_places, previous_char=1):
	if vacent_places==0:
		return 0
	if vacent_places==1:
		if previous_char:
			return 2
		else:
			return 1
	if previous_char:
		return count_binary_strings_recursion(vacent_places - 1, 1) + count_binary_strings_recursion(vacent_places - 1, 0)
	else:
		return count_binary_strings_recursion(vacent_places - 1, 1)



def count_binary_strings_bpdp(dp0, dp1):
	for k in range(len(dp0)):
		if k == 0:
			pass
		elif k == 1:
			dp0[k], dp1[k] = 1, 2
		else:
			dp0[k], dp1[k] = dp1[k-1], dp0[k-1] + dp1[k-1]
	return dp1[-1]

if __name__ == '__main__':
	N = 4
	dp0 = [0] * (N + 1)
	dp1 = [0] * (N + 1)
	print(count_binary_strings_bpdp(dp0, dp1))

	print(count_binary_strings_recursion(4, 1))