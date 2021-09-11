def helperMoneyLooted(houses, n, dp):
	if n == 1:
		return houses[0]
	if n == 2:
		return max(houses[0], houses[1])
	dp[0] = houses[0]
	dp[1] = houses[1]
	for i in range(2, n):
		maxa = -1
		for j in range(i-1):
			maxa = max(maxa, dp[j])
		dp[i] = maxa + houses[i]
	return max(dp[-1], dp[-2])
        

def maxMoneyLooted(houses, n) :
	dp = []
	for i in houses:
		dp.append(-1)
	ans = helperMoneyLooted(houses, n, dp)
	return ans


if __name__ == '__main__':
	arr = [5, 5, 10, 100, 10, 5]
	print(maxMoneyLooted(arr, len(arr)))