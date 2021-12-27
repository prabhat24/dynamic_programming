


def min_paint_cost_recursion(arr, ind, color):
	if ind < 0:
		return 0
	elif color == 'b':
		result = min(
				min_paint_cost_recursion(arr, ind-1, 'r'),
				min_paint_cost_recursion(arr, ind-1, 'g')
			) + arr[ind][1]
	elif color == 'g':
		result = min(
				min_paint_cost_recursion(arr, ind-1, 'r'),
				min_paint_cost_recursion(arr, ind-1, 'b')
			) + arr[ind][2]
	elif color == 'r':
		result = min(
				min_paint_cost_recursion(arr, ind-1, 'b'),
				min_paint_cost_recursion(arr, ind-1, 'g')
			) + arr[ind][0]
	return result

def paint_cost_driver_recursion(arr, ind):
	return min(min_paint_cost_recursion(arr, ind, 'b'), min_paint_cost_recursion(arr, ind, 'r'), min_paint_cost_recursion(arr, ind, 'g'))

#####################################################################

def min_paint_cost_bpdp(arr):
	r = 0
	b = 0
	g = 0
	for k in range(len(arr)):
		if k == 0:
			r = arr[0][0]
			b = arr[0][1]
			g = arr[0][2]
		else:
			r, b, g = min(b, g) + arr[k][0], min(r, g) + arr[k][1], min(r, b) + arr[k][2]
	return min(r, b, g)


if __name__ == '__main__':
	arr = [
		(1, 5, 7),
		(5, 8, 4),
		(3, 2, 9),
		(1, 2, 4)
	]
	print(paint_cost_driver_recursion(arr, len(arr)-1))
	print(min_paint_cost_bpdp(arr))
