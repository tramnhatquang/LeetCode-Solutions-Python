def myFunction(n, m):
	return n * m


print(myFunction(34, 4))


# nested functions have access to outer variables
def outer(a, b):
	c = 'c'

	def inner():
		return a + b + c

	return inner()


print(outer('a', 'b'))
