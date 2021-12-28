def subsequences_count(string):
	a, ab, abc = 0, 0, 0
	
	for k in string:
		if k == 'a':
			a = 2 * a + 1
		elif k == 'b':
			ab = 2 * ab + a

		elif k == 'c':
			abc = 2 * abc + ab 
	return abc


if __name__ == '__main__':
	string = 'abcabc'
	print(subsequences_count(string))