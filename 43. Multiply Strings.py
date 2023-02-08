class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        """
        Sum the product of all pairs from each digit
        Overview: For each digit in num2, we multiply it to each digit in nums1 and continue to add them together
        The number of digits of the result <= nums1.length + nums2.length so using an arr of size (N + M) is enough to hold our res

        Notice that (i1 + i2)-th will have the ones place of the result, and the tens place of the result (carry) will be added to (i1 + i2 + 1)-th place
        """
        if num1 == '0' or num2 == '0':
            return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]
        n, m = len(num1), len(num2)
        res = [0] * (n + m)

        for i1 in range(n):
            for i2 in range(m):
                # the index depends on the place of i1 in the nums1 and i2 in the nums2
                index = i1 + i2
                # the digit currently at the position index in the answeer string is carried over and summed with the current result
                carry = res[index]
                multiplication = int(num1[i1]) * int(num2[i2]) + carry

                # set the ones place of the multiplication  result
                res[index] = multiplication % 10
                res[index + 1] += multiplication // 10

        # pop the excess 0 from the end of answer
        if res[-1] == 0:
            res.pop()
        print(f'Res: {res}')
        return ''.join(map(str, res[::-1]))

        # time: O(n * m), n, m are lengths of nums1, nums2 respsectively
        # space: O(n + m)

	def multiply_not_accepted(self, num1: str, num2: str) -> str:
		# approach 1: Use the built in int() function to covert these strings into numbers, find the multiplication and then conver the result back to string

		# Not acceptable and it conflicts with the requirements
		# time: O(N * M) where N,M are lengths of num1, num2 respectively
		# return str(int(num1) * int(num2))

		# approach 2: Convert each string into the number and conver the result back into string
		if num1 == '0' or num2 == '0':
			return '0'

		def decode(num: str) -> int:
			ans = 0
			for i in num:
				ans = ans * 10 + (ord(i) - ord('0'))
			return ans

		def encode(num: int) -> str:
			res = ''
			while num:
				least_digit = num % 10
				num //= 10
				res = chr(ord('0') + least_digit) + res

			return res

		return encode(decode(num1) * decode(num2))
