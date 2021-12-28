def decodable(string):
	if string[0] == '0':
		return False
	elif int(string) >= 1 and int(string) <=  25:
		return True
	return False



def count_encodings(string):
	dp = [0] * (len(string) +1)
	dp[0] = 1
	for k in range(len(string)):
		if k == 0:
			if decodable(string[k]):
				dp[k+1] = 1
		else:
			if decodable(string[k]):
				dp[k+1] = dp[k]
			if decodable(string[k-1] + string[k]):
				dp[k+1] = dp[k+1] + dp[k-1]
	print(dp[-1])

if __name__ == '__main__':
	string = "1222"
	count_encodings(string)
