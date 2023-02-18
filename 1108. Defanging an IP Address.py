class Solution:

    def defangIPaddr_optimal(self, address: str) -> str:
        res = []
        left = 0
        n = len(address)
        while left < n:
            if address[left] != '.':
                res.append(address[left])
            else:
                res.append('[.]')
            left += 1
        return ''.join(res)

        # time = space = O(N)
    def defangIPaddr_built_in(self, address: str) -> str:
        # using the built-in function
        return address.replace('.', '[.]')
        # time = space = O(n)
