class Solution:

    def arraysIntersection_optimal(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """
        The optimal solution is to use Three Pointer Approach
        Algo:
            1. Intialize three points p1, p2, p3 which point to the first index of each arr.
            2. 
            - Each time, we want to increment the pointer that points to the smallest number, i.e., min(arr1[p1], arr2[p2], arr3[p3]) forward;
            - if the numbers pointed to by p1, p2, and p3 are the same, we should then store it and move all three pointers forward.
        """
        p1 = p2 = p3 = 0
        res = []

        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                res.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                # move pointer which points to the smaller number
                if arr1[p1] < arr2[p2]:
                    p1 += 1
                elif arr2[p2] < arr3[p3]:
                    p2 += 1
                else:
                    p3 += 1
        return res

        # time: O(n), n is the total inputs
        # space: O(1)

    def arraysIntersection_brute_force(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # Starting from Python 3.7, Counter is a subclass of dict so it will remember the insertion
        counter = collections.Counter(arr1 + arr2 + arr3)
        res = []
        for key, count in counter.items():
            if count == 3:
                res.append(key)
        return res

        # time = space = O(n), n is total length of all inputs

    def arraysIntersection_not_clean(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """
        -  Find all the common numbers in arr1 and arr2 first
        - Store all common numbers from arr1, arr2 in a res List
        - COmpare all numbers in the arr3, if there are number not in res, remove it
        """
        p1 = len(arr1) - 1
        p2 = len(arr2) - 1
        common_numbers_12 = []
        while p1 >= 0 and p2 >= 0:
            if arr1[p1] == arr2[p2]:
                common_numbers_12.append(arr1[p1])
                p1 -= 1
                p2 -= 1
            elif arr1[p1] > arr2[p2]:
                p1 -= 1
            else:
                p2 -= 1

        common_numbers_12.reverse()
        print(f'Common numbers betweeen arr1, arr2: {common_numbers_12}')
        # common_numbers_12.reverse()
        res = []
        p3 = len(arr3) - 1
        p4 = len(common_numbers_12) - 1
        while p4 >= 0 and p3 >= 0:
            if common_numbers_12[p4] == arr3[p3]:
                res.append(arr3[p3])
                p3 -= 1
                p4 -= 1
            elif common_numbers_12[p4] < arr3[p3]:
                p3 -= 1
            else:
                p4 -= 1

        print(f'Res: {res}')
        res.reverse()
        return res
