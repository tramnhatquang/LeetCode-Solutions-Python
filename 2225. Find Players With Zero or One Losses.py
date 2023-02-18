class Solution:
    def findWinners_hash_map(self, matches: List[List[int]]) -> List[List[int]]:
        """
        Use a hash map to count the losses for each player
        """
        map_losses_count = {}
        for winner, loser in matches:
            # update the loss count of loser by 1
            # for winner, if they have at least 1 loss, do nothing. Otherwise, we update their loss as 0 to indicate that they already played at least one game
            map_losses_count[winner] = map_losses_count.get(winner, 0)
            map_losses_count[loser] = map_losses_count.get(loser, 0) + 1

        print(f'Map: {map_losses_count}')

        # use 2 lists to append the no lose players, and one lose players
        zero_lose, one_lose = [], []
        for player, lose in map_losses_count.items():
            if lose == 0:
                zero_lose.append(player)
            elif lose == 1:
                one_lose.append(player)

        return [sorted(zero_lose), sorted(one_lose)]

        # time: O(n log n) for TC
        # space: O(n) due to sorting

    def findWinners_counting_sort(self, matches: List[List[int]]) -> List[List[int]]:
        """
        The more optimal solution is to use COunting sort but this apporach is only applied when the  input is in a samll valid range (i.e. 1 <= matches.length <= 10^5)
        More info:
        https://leetcode.com/problems/find-players-with-zero-or-one-losses/solutions/2655744/official-solution/
        """
        losses_count = [-1] * 100001

        for winner, loser in matches:
            if losses_count[winner] == -1:
                losses_count[winner] = 0
            if losses_count[loser] == -1:
                losses_count[loser] = 1
            else:
                losses_count[loser] += 1

        answer = [[], []]
        for i in range(100001):
            if losses_count[i] == 0:
                answer[0].append(i)
            elif losses_count[i] == 1:
                answer[1].append(i)

        return answer

        # time: O(n + k), n is the number of matches, k is the range of values in winner, loser
        # space: O(k) for the arr
