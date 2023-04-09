def minStep(str) -> int:
	charX = 'X'
	numY = 0
	minDel = 0
	for i in range(0, len(str)):
		if (charX == str[i]):
			minDel = min(numY, minDel + 1)
		else:
			numY += 1
	# print(f'Res: {minDel}')
	return minDel


def min_removals(s: str) -> int:
	x_count = 0
	y_count = 0
	min_removals_needed = 0

	for c in s:
		if c == 'X':
			x_count += 1
		elif c == 'Y':
			y_count += 1
			min_removals_needed = min(+ 1, x_count)

	return min_removals_needed


if __name__ == '__main__':
	# assert minStep('YX') == 1
	# assert minStep('YXXXYXY') == 2
	# assert minStep('YYXYXX') == 3
	# assert minStep('XXYYYY') == 0

	# assert min_removals('YXXXYXY') == 2
	# assert min_removals('YYXYXX') == 3
	# assert min_removals('XXYYYY') == 0
	# assert min_removals('YYXXYYXY') == 3
	# assert min_removals('XXYYXYXYXYXYXYXYYYYXYYYXYYY') == 8
	# assert min_removals('YYYYYYYYYY') == 0
	# assert min_removals('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') == 0

	map = {'a': '2', 'b': '3'}
	print(map)
