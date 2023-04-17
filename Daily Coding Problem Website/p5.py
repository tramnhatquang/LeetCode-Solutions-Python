"""
Good morning!

Here's a solution to yesterday's problem.

This is your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

***** Implement car and cdr
"""


def cons(a, b):
	def pair(f):
		return f(a, b)

	return pair


def car(pair):
	def first(a, b):
		return a

	return pair(first)


def cdr(pair):
	def last(a, b):
		return b

	return pair(last)


"""
This is a really cool example of using closures to store data. We must look at the signature type of cons to retrieve its first and last elements. cons takes in a and b, and returns a new anonymous function, which itself takes in f, and calls f with a and b. So the input to car and cdr is that anonymous function, which is pair. To get a and b back, we must feed it yet another function, one that takes in two parameters and returns the first (if car) or last (if cdr) one.
"""

if __name__ == '__main__':
	# test examples
	print(car(cons(1, 2)))  # 1
	print(cdr(cons(3, 4)))  # 4
