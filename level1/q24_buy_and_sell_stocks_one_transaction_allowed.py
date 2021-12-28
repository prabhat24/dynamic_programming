def oneTransaction(arr, n):
    global_maxa = 0
    for i in range(n):
        maxa = 0
        for k in range(i+1, n):
    	    diff = arr[k] - arr[i]
    	    maxa = max(maxa, diff)
        global_maxa = max(maxa, global_maxa)
    print(global_maxa)


if __name__ == '__main__':
	arr = [11, 6, 7, 19, 4, 1, 6, 18, 4]
	oneTransaction(arr, len(arr))