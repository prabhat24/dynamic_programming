def min_paint_cost_bpdp(arr):
	dp = [[0] * len(arr[0]) for r in arr]
	for house_id in range(len(arr)):
		if house_id == 0:
			for j, c in enumerate(arr[house_id]):
				dp[house_id][j] = c
		else:
			# r, b, g = min(b, g) + arr[k][0], min(r, g) + arr[k][1], min(r, b) + arr[k][2]
			for j, c in enumerate(arr[house_id]):
				lst = [dp[house_id-1][f] if f!=j else (1<<32 -1)for f in range(0, len(arr[0]))]
				dp[house_id][j] = min(lst) + c
	return min(dp[-1])


if __name__ == '__main__':
	arr = [
		(1, 5, 7),
		(5, 8, 4),
		(3, 2, 9),
		(1, 2, 4)
	]
	print(min_paint_cost_bpdp(arr))	