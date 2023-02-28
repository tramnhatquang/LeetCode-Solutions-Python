import collections
from typing import *


class Solution:
    
    """We can use Disjoint Set to solve this prob
    """
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # APPROACH 1: Brute force solution
        # 1. For each pair of account, we check if any pairs of emails of these accounts are the same. We continue to do that until we check all the accounts
        # However, this approach is inefficient due to the high time compleixty
        # TC = (N*M*L)^2, N is the number of accounts, M is the number of emails per account, L is the length of each email

        # APPROACH 2: DFS
        # One account can have multiple emails, but two similar emails only belong to one person
        # We can see that the set of emails of each account form a single group belonging to a person. If we visualize these as a graph, we can think of them as various connected components of a graph. More specifically, the emails belonging to a person form the node of a connected component and all these connected components make up our whole graph.

        # Now, each email from one account will have an edge with one another email of the same account. But if an email is found in multiple accounts, they will have edge with other emails from all these multiple accounts as well. The following diagram will help better visualize the scenario (In image, A is input list, Pi denotes person name of an account and Ei denotes emails) -

        # make edges between emails among a same account holder
        graph = collections.defaultdict(set)
        visited = set()

        # build a adjacent list, add edges between first and rest email within each list
        for account in accounts:
            first_email = account[1]
            for i in range(2, len(account)):
                graph[first_email].add(account[i])
                graph[account[i]].add(first_email)

        # using DFS to find next edges
        def dfs(email: str, merged_list: List[str]):
            visited.add(email)
            merged_list.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, merged_list)

        # traverse to get all emails belonging to a same person
        res = []
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email not in visited:
                merged_list = []
                dfs(first_email, merged_list)
                res.append([name] + sorted(merged_list))
        return res

        # time: O(NK log(NK)) where N is length of accounts, K is the max length of an account
        # space: O(NK)
