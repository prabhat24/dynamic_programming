# Given an array of n integers (non-negative), and a target value tar, you need to check whether a subset of the array whose sum of elements is equal to the target tar exists or not.
# Please recall that a subset (or subsequence) of an array is taking zero or more elements from the array (in the same order in which they occur in the array).
# Here, you need to just print true or false whether such a target sum subset exists or not. You do not need to print the subset.


# Example, for array = {4, 2, 7, 1, 3} and target = 10, the answer will be true as there exists a subset {7, 3} whose sum = target.
# There can be other subsets also like {4, 2, 1, 3} whose sum = target = 10, but as soon as we find any one subset, we can print true.


def target_sum_recursion(r, wt, arr):
	if wt == 0:
		return True
	if r == 0 and wt>0:
		return False
	if wt - arr[r] >= 0:
		return target_sum_recursion(r-1, wt, arr) or target_sum_recursion(r-1, wt - arr[r], arr)
	else:
		return False

def target_sumbpdp(dp, weight, arr):
	for r in range(len(dp)):
		for c in range(len(dp[0])):
			if c == 0:
				dp[r][c] = True
			elif r == 0:
				dp[r][c] = False
			else:
				dp[r][c] = dp[r-1][c] or dp[r-1][c-arr[r]]
	return dp[len(arr)-1][weight]

if __name__ == '__main__':
	arr = [4, 2, 7, 1]
	arr.insert(0, 0)
	print(target_sum_recursion(len(arr) - 1, 10, arr))

	weight = 10
	dp = [[-1] * (weight + 1) for k in range(len(arr))]
	print(target_sumbpdp(dp, weight, arr))