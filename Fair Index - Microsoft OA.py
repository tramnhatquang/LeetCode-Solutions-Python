def fairIndexes(A: List[int], B: List[int]) -> int:

    sumA, sumB = sum(A), sum(B)
    # evaluate if their sums are equal to each other or not. If they are not, return 0
    if sumA != sumB:
        return 0

    # since we split two arrays into 4 non-empty subarrays so we can ignore the first and last index
    # find the prefix sum up to the i-th index and check if it is equal to the remaining sum and other prefixes,
    # if it does, then increase the count by 1
    prefix_a, prefix_b = 0, 0
    res = 0
    for i in range(len(A) - 1):
        prefix_a += A[i]
        prefix_b += B[i]
        if prefix_a == prefix_b == sumA - prefix_a == sumB - prefix_b:
            res += 1

    return res
    # time = O(n)
    # space: O(1)
