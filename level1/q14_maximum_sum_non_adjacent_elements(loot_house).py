

def loot_houses_recursion(arr, ind):
	if ind == 0:
		return arr[ind]
	elif ind == 1:
		return max(arr[ind-1], arr[ind])
	else:
		inc = loot_houses_recursion(arr, ind-2) + arr[ind]
		exc = loot_houses_recursion(arr, ind-1)
		return max(inc, exc)


def loot_houses_bpdp_m1(arr):
	inc = 0
	exc = 0

	for k in range(len(arr)):
		if k == 0:
			inc, exc = arr[k], 0
		else:
			inc, exc = exc + arr[k], max(inc, exc)
	return max(inc, exc)

def loot_houses_bpdp_m2(arr):
	dp = [0] * len(arr)
	for k in range(len(arr)):
		if k == 0:
			dp[k] = arr[k]
		if k == 1:
			dp[k] = max(arr[k], arr[k-1])
		else:
			dp[k] = max(dp[k-2] + arr[k], dp[k-1])
	result = max(dp[-1], dp[-2]) if len(arr) > 1 else arr[0]
	return result


if __name__ == '__main__':
	arr = [5, 10, 10, 100, 5]
	print(loot_houses_recursion(arr, len(arr)-1))
	print(loot_houses_bpdp_m1(arr))
	print(loot_houses_bpdp_m2(arr))

