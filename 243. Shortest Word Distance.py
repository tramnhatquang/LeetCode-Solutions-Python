class Solution:
    def shortestDistance_optimal(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """
        Optimal solution: Linear scan thr the array string
        1. We use two pointers p1, p2 which indicate the last seen index of each word respectively. Initialize them as p1 = p2 = -1.
        2. We iterate thr each word in the string.
            - If the word matches word1 or word2,  If it matches word1, we can update p1 to the current index, and if p2 is not -1, we can calculate the distance between p1 and p2 and update minDistance if the distance is smaller than the current value of minDistance. Similarly, if the string matches word2, we can update p2 and calculate the distance.
        """
        n = len(wordsDict)
        min_distance = n
        p1 = p2 = -1
        for i in range(n):
            if wordsDict[i] == word1:
                p1 = i
                if p2 != -1:
                    min_distance = min(min_distance, abs(p1 - p2))
            elif wordsDict[i] == word2:
                p2 = i
                if p1 != -1:
                    min_distance = min(min_distance, abs(p1 - p2))

        return min_distance


def shortestDistance_brute_force(self, wordsDict: List[str], word1: str, word2: str) -> int:
    """
    Brute force solution is to find all possible differences between the locations of each word in the dictionary.
    - TC: O(n^2) -> not time efficient,
    - space complexity: O(1)
    """
    n = len(wordsDict)
    min_distance = n
    for i in range(n):
        if wordsDict[i] == word1:
            for j in range(n):
                if wordsDict[j] == word2:
                    min_distance = min(min_distance, abs(i - j))

    return min_distance
