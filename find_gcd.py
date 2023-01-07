def gcd(a: int, b: int) -> int:
	# euclidean algo with mod operator
	if b == 0:
		return a
	return gcd(b, a % b)


# time: O(log(min(a, b)))
# space: O(n) n = max(a, b)

def gcd_1(a: int, b: int) -> int:
	# euclidean algo with differences
	# replace the larger number with the diff between numbers
	if a == b:
		return b
	if a > b:
		return gcd(a - b, b)
	return gcd(a, b - a)


if __name__ == '__main__':
	assert gcd(17, 11) == 1
	assert gcd(12, 48) == 12
	assert gcd(11, 17) == 1
