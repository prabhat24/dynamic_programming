def l_subse(array, prev, ittr):
	if ittr == len(array):
		return 0
	else:
		inc, exc = 0, 0
		if prev < array[ittr]:
			inc = 1 + l_subse(array, array[ittr], ittr + 1)
		exc = l_subse(array, prev, ittr + 1)
		return max(inc, exc)

def lis(array):
	min_int = -1
	return l_subse(array, -1, 0)

if __name__ == "__main__":
	array = [10, 22, 9, 33, 21, 50, 41, 60, 80, 1]
	ittr = 0
	print(lis(array))