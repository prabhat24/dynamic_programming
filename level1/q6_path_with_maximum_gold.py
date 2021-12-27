

def max_gold_recursion(mine, r, c, R, C):
	if r<0 or r>=R or c<0 or c>=C:
		return -1
	if c==0:
		return mine[r][c]
	return max( max_gold_recursion(mine, r-1, c-1, R, C), max_gold_recursion(mine, r, c-1, R, C), max_gold_recursion(mine, r+1, c-1, R,C)  ) + mine[r][c]

def max_gold_recursion_driver(mine, R, C):
	max_gold = 0
	for row in range(0, R):
		max_gold = max(max_gold_recursion(mine, row, C-1, R, C), max_gold)
	return max_gold

################################################################

def max_gold_tpdp(dp, mine, r, c, R, C):
	if r<0 or r>=R or c<0 or c>=C:
		return -1
	if c==0:
		return mine[r][c]
	if dp[r][c] != -1:
		return dp[r][c]
	dp[r][c] = max( max_gold_recursion(mine, r-1, c-1, R, C), max_gold_recursion(mine, r, c-1, R, C), max_gold_recursion(mine, r+1, c-1, R,C)  ) + mine[r][c]
	return dp[r][c]

def max_gold_tpdp_driver(dp, mine, R, C):
	max_gold = 0
	for row in range(0, R):
		max_gold = max(max_gold_tpdp(dp, mine, row, C-1, R, C), max_gold)
	return max_gold

###################################################################

def max_gold_bpdp(dp, mine, R, C):
	for r in range(0, R):
		dp[r][0] = mine[r][0]

	for c in range(1, C):
		for r in range(0, R):
			if r == 0:
				dp[r][c] = max(dp[r][c-1], dp[r+1][c-1]) + mine[r][c]
			elif r == R - 1:
				dp[r][c] = max(dp[r-1][c-1] , dp[r][c-1]) + mine[r][c]
			else:
				dp[r][c] = max([dp[r-1][c-1], dp[r][c-1], dp[r+1][c-1]]) + mine[r][c]
	maxa = 0
	for r in range(0, R):
		maxa = max(dp[r][C-1], maxa)
	return maxa


#################################################################
if __name__ == '__main__':
	mine = [[0, 1, 4, 2, 8, 2],
			[4, 3, 6, 5, 0, 4],
			[1, 2, 4, 1, 4, 6],
			[2, 0, 7, 3, 2, 2],
			[3, 1, 5, 9, 2, 4],
			[2, 7, 0, 8, 5, 1],]
	print(max_gold_recursion_driver(mine, len(mine), len(mine[0])))

	dp = [[-1] * len(mine[0]) for k in range(len(mine))]
	print(max_gold_tpdp_driver(dp, mine, len(mine), len(mine[0])))

	dp = [[-1] * len(mine[0]) for k in range(len(mine))]
	print(max_gold_bpdp(dp, mine, len(mine), len(mine[0])))


