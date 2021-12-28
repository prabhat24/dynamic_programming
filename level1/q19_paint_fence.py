
def paint_fence(colors, houses):
	ii = 0
	ij = 0
	for house_id in range(1, houses+1):
		if house_id == 1:
			ii, ij = 0, colors
		elif house_id == 2:
			ii, ij = colors, colors*(colors-1)
		else:
			ii, ij = ij, (ii + ij)*(colors-1)
	return ii + ij


if __name__ == '__main__':
	colors = 3
	houses = 5
	print(paint_fence(colors, houses))
