def coin_change_recursion(amt, arr, N):
	if amt == 0:
		print("here")
		return 0
	i = 0
	mina = 1<<32 -1
	while arr[i] <= amt and i < N:
		val_ittr = coin_change_recursion(amt-arr[i], arr, N)
		mina = min(val_ittr, mina)
		i+=1
	return mina + 1


def coin_change_tpdp(dp, amt, arr, N):
	if amt == 0:
		dp[amt] = 0
		return 0
	if dp[amt] != -1:
		return dp[amt]
	i = 0
	mina = 1<<32 -1
	while arr[i] <= amt and i < N:
		val_ittr = coin_change_tpdp(dp, amt-arr[i], arr, N)
		mina = min(val_ittr, mina)
		i+=1
	dp[amt] = mina + 1
	return dp[amt]

def coin_change_bpdp(dp, amt, arr, N):
	dp[0] = 0
	for a in arr:
		if a <= amt:
			dp[a] = 1
	print(dp)
	for i in range(1, amt+1):
		if dp[i] != 1:
			k = 0
			mina = 1<<32 -1
			while k < N and arr[k] <= i:
				val_ittr = dp[i - arr[k]]
				mina = min(val_ittr, mina)
				k +=1
			dp[i]= mina + 1
			print(dp)
	return dp[-1]

if __name__ == '__main__':
	arr = [1,7,10]
	amt = 15
	dp = [-1] * (amt +1)
	N = len(arr)
	# print(coin_change_recursion(amt, arr, N))
	print(coin_change_bpdp(dp, amt, arr, N))

