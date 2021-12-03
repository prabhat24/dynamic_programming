
def max_price(arr, i, j):

	if i>j:
		return 0

	maxa = 0
	for k in range(i, j+1):
		if k == i and k == j:
			inc = arr[k]
		elif k == i and i+1 <= j:
			inc = arr[k] + arr[k + 1]
		elif k == j and k-1 >= i:
			inc = arr[k] + arr[k-1]
		elif k > i and k < j:
			inc = arr[k-1] + arr[k] + arr[k+1]
		each_ans = max_price(arr, i, k-1) + max_price(arr, k+1, j) + inc
		maxa = max(maxa, each_ans)
	return maxa


if __name__ == '__main__':
	arr = [1,2,3,4]
