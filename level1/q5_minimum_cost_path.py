
def min_cost_path_recursion(ground, r, c, R, C):
	if r==R - 1  and c==C -1:
		return ground[R - 1][C - 1]
	if r >= R or c >= C:
		return 1<<32 -1
	return min(min_cost_path_recursion(ground, r+1, c, R, C), min_cost_path_recursion(ground, r, c+1, R, C)) + ground[r][c]


def min_cost_path_tpdp(dp, ground, r, c, R, C):
	if r==R - 1  and c==C -1:
		return ground[R - 1][C - 1]
	if r >= R or c >= C:
		return 1<<32 -1
	if dp[r][c] != -1:
		return dp[r][c]
	dp[r][c] =  min(min_cost_path_tpdp(dp, ground, r+1, c, R, C), min_cost_path_tpdp(dp, ground, r, c+1, R, C)) + ground[r][c]
	return dp[r][c]

def min_cost_path_bpdp(dp, ground,  R, C):
	for r in range(R-1, -1, -1):
		for c in range(C-1, -1, -1):
			if r + 1 >= R and c + 1 >= C:
				dp[r][c] = ground[r][c]
			elif r + 1 >= R:
				dp[r][c] = dp[r][c+1] + ground[r][c]
			elif c + 1 >= C:
				dp[r][c] = dp[r+1][c] + ground[r][c]
			else:
				dp[r][c] = min(dp[r+1][c], dp[r][c+1]) + ground[r][c]
	return dp[0][0]


if __name__ == '__main__':
	ground = [[0, 1, 4, 2, 8, 2],
			[4, 3, 6, 5, 0, 4],
			[1, 2, 4, 1, 4, 6],
			[2, 0, 7, 3, 2, 2],
			[3, 1, 5, 9, 2, 4],
			[2, 7, 0, 8, 5, 1],]

	print(min_cost_path_recursion(ground, 0, 0, len(ground), len(ground[0])))

	dp = [[-1] * len(ground[0]) for k in range(len(ground))]
	print(min_cost_path_tpdp(dp, ground, 0, 0, len(ground), len(ground[0])))


	dp = [[-1] * len(ground[0]) for k in range(len(ground))]
	print(min_cost_path_bpdp(dp, ground,  len(ground), len(ground[0])))