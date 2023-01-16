if __name__ == '__main__':
	a = [[6, 9], [1, 100], [6, 1000]]
	a.sort(key=lambda x: [x[0], -x[1]])

	print(a)
