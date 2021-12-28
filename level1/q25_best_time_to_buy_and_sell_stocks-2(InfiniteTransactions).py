# 1. You are given a number n, representing the number of days.
# 2. You are given n numbers, where ith number represents price of stock on ith day.
# 3. You are required to print the maximum profit you can make if you are allowed infinite transactions.
# Note - There can be no overlapping transaction. One transaction needs to be closed (a buy followed by a sell) before opening another transaction (another buy)



def max_profit(arr, N):
	buy_ptr = 0
	sell_ptr = 0
	profit = 0
	arr.append(0)
	for ptr in range(1, N+1):
		if arr[ptr] >= arr[sell_ptr]:
			sell_ptr = ptr
		if arr[ptr] < arr[sell_ptr]:
			profit += arr[sell_ptr] - arr[buy_ptr]
			buy_ptr = ptr
			sell_ptr = ptr
	print(profit)

if __name__ == 'main':
	arr = [5, 2, 0, 2, 1, 2, 0, 7]
	max_profit(arr, len(N))