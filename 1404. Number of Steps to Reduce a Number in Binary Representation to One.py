class Solution:

    def numSteps_optimal(self, s: str) -> int:
        # Intuition is that odd numbers has 1 in the last digit, on the other hands, even numbers has 0 in the last digit.
        # stimulate the step like the given instruction
        # processing the string from right to left, until the string has only one digit

        # Algo:
        # 1. Initialize the count = carry = 0
        # 2. Processing the string from the last digit to the begining [n - 1...1], except the first digit
        #   - if s[i] + carry == 1 -> it's an odd number, we need two operations: add 1 and divide by two, count += 2
        #   - if s[i] + carry = 0 -> it's an even number, we need 1 operation: divide by two, count += 1
        # 3. Finally, if carry = 1, then s[0] + carry = 2, need one additional operation divide by 2 to become one, else if carry = 0, then total = s[0] + carry = 1, no need any additional operation (return count + carry)
        count = carry = 0
        n = len(s)
        for i in range(n - 1, 0, -1):
            if int(s[i]) + carry == 1:  # Odd number
                count += 2
                carry = 1
            else:
                count += 1
        return count + carry
        # time: O(n), space: O(1)

    def numSteps_built_in(self, s: str) -> int:
        # convert the binary string to number
        # do the stimulation based on the given instructions

        number = int(s, 2)
        print(f'Number: {number}')
        count = 0
        while number != 1:
            if number % 2 == 0:
                number //= 2
            else:
                number += 1
            count += 1

        return count
        # time: O(log (number))
        # space: O()
