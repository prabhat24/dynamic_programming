# 1. You are given a number n, representing the number of days.
# 2. You are given n numbers, where ith number represents price of stock on ith day.
# 3. You are required to print the maximum profit you can make if you are allowed infinite transactions.
# Note - There can be no overlapping transaction. One transaction needs to be closed (a buy followed by a sell) before opening another transaction (another buy)

from typing import List


# based on solution taught by Sumit Sir. check his video
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

# more optimized way of seeing/solving the problem. Please check this once you have solved it using above method.
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solutions/5816678/video-sell-a-stock-immediately
def maxProfit(prices: List[int]) -> int:
    N = len(prices)
    B = 0
    S = 0
    amt = 0

    # making B = i when prices[S] < prices[B]
    for i in range(N):
        S = i

        if prices[S] > prices[B]:
            print("profit", f"day {i}", prices[S] - prices[B] )
            amt += prices[S] - prices[B]
        B = i
    print(amt)
    return amt

if __name__ == 'main':
	arr = [5, 2, 0, 2, 1, 2, 0, 7]
	max_profit(arr, len(N))