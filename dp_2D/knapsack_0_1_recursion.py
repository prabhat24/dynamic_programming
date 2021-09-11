def max_val(cur, W, val_arr, wt_arr):
	if cur == len(val_arr):
		return 0
	else:
		inc, exc = 0,0
		if W-wt_arr[cur] >= 0:
			inc = val_arr[cur] + max_val(cur + 1, W - wt_arr[cur], val_arr, wt_arr)
		exc = max_val(cur + 1, W, val_arr, wt_arr)
		return max(inc, exc)
if __name__ == '__main__':
	val_arr = [5, 20, 20, 10]
	wt_arr = [2, 7,3, 4]
	W =11
	print(max_val(0, W, val_arr, wt_arr))
