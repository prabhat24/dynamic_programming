# PROBLEM STATEMENT
# You are given n representing the number of stairs.
# You are on the 0th step and are required to climb to the top.
# You are given n numbers, where i-th element's value represents - till how far from the step you could jump to in a single move.
# You are required to print the number of different paths via which you can climb to the top.

def climb_recursion(arr, src, dest):
	if src > dest:
		return 0
	if src == dest:
		return 1
	
	ans = 0
	for k in range(1, arr[src]+1):
		ans += climb_recursion(arr, src+k, dest)
	return ans


def climb_tpdp(dp, arr, src, dest):
	if src > dest:
		return 0
	if src == dest:
		return 1
	if dp[src] != -1:
		return dp[src]
	ans = 0
	for k in range(1, arr[src]+1):
		ans += climb_tpdp(dp, arr, src+k, dest)
	dp[src] = ans
	return dp[src]

def climb_bpdp(dp, arr, src, dest):
	dp[dest] = 1
	for i in range(dest - 1, -1, -1):
		jumps_at_ith_step = arr[i]
		ith_ans = 0
		for k in range(1, jumps_at_ith_step + 1):
			if i + k <= dest:
				ith_ans+=dp[i+k]
		dp[i] = ith_ans
	return dp[0]

	

if __name__ == '__main__':
	jumps_arr = [2, 4, 1, 0, 2, 3]
	print(climb_recursion(jumps_arr, 0, 6))
	dp = [-1] * (len(jumps_arr) + 1)
	print(climb_tpdp(dp, jumps_arr, 0, 6))
	dp = [-1] * (len(jumps_arr) + 1)
	print(climb_bpdp(dp, jumps_arr, 0, 6))