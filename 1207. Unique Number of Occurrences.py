class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = defaultdict(int)
        for num in arr:
            map[num] += 1

        # count the number of distinct values
        count = 0
        for i in range(len(set(map.values()))):
            count += 1
        return len(map) == count
    
    # time: O(n) = space, n is number of elements
    

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter) == len(set(counter.values()))

    # time: O(n) = space, n is number of elements