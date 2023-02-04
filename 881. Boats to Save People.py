from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
            If the heaviest person can share a boat with the lightest person, then do so. Otherwise, the heaviest person can't pair with anyone, so they get their own boat.

            The reason this works is because if the lightest person can pair with anyone, they might as well pair with the heaviest person.
        """
        people.sort()
        res = 0
        left, right = 0, len(people) - 1
        while left <= right:
            remain = limit - people[right]
            right -= 1
            res += 1
            if left <= right and remain >= people[left]:
                left += 1
        return res
        # time: O(n log n), space: O(n) due to sorting
