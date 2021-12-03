
def palindrome(arr, st, end):
	ptr1 = st
	ptr2 = end
	while ptr1 < ptr2:
		if arr[ptr1] != arr[ptr2]:
			return False
		ptr1 +=1
		ptr2 -=1
	return True

def min_palindrome_partitioning_recursion(arr, st, end):
	if palindrome(arr, st, end):
		return 0

	mini = 1<<32-1
	for k in range(st, end):
		lt = min_palindrome_partitioning_recursion(arr, st, k)
		rt = min_palindrome_partitioning_recursion(arr, k+1, end)
		ans = lt + rt + 1
		mini = min(ans, mini)
	return mini

if __name__ == '__main__':

	arr = 'ababbbabbababa'
	print(min_palindrome_partitioning_recursion(arr, 0, len(arr)-1))