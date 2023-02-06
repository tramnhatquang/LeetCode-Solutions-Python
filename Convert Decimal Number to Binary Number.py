
"""Solution Review: Convert Decimal Number to Binary Number
    """


def decimalToBinary(number):
    
    # keep diving the number by 2 until we are left with 1
    # since 1 divided by 2 gives remainder 1; this will be our base case
    # Base Case
    if number <= 1:
        return str(number)

    # Recursive Case
    else:
        # Floor division -
        return decimalToBinary(number // 2) + decimalToBinary(number % 2)
        # division that results into whole number adjusted to the left in the number line


# Driver Code
testVariable = 11
print(decimalToBinary(testVariable))
