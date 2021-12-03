
def c_recursion(str1, st, end):
	if st > end:
		return 0
	if st == end:
		return 1
	if str1[st] == str1[end]:
		ans = c_recursion(str1, st+1, end) + c_recursion(str1, st, end-1) + 1
	else:
		ans = c_recursion(str1, st+1, end) + c_recursion(str1, st, end-1) - c_recursion(str1,  st + 1, end - 1)
	print(st, end, ans)
	return ans

if __name__ == '__main__':
	str1 = "abcb"
	ans = c_recursion(str1, 0, len(str1)-1)
	print(ans)