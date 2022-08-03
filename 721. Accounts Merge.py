from typing import *

class Solution:
	def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
		# APPROACH 1: Brute force solution
		# 1. For each pair of account, we check if any pairs of emails of these accounts are the same. We continue to do that until we check all the accounts
		# However, this approach is inefficient due to the high time compleixty
		# TC = (N*M*L)^2, N is the number of accounts, M is the number of emails per account, L is the length of each email

		# APPROACH 2: DFS
		# One account can have multiple emails, but two similar emails only belong to one person
		# We can see that the set of emails of each account form a single group belonging to a person. If we visualize these as a graph, we can think of them as various connected components of a graph. More specifically, the emails belonging to a person form the node of a connected component and all these connected components make up our whole graph.

		# Now, each email from one account will have an edge with one another email of the same account. But if an email is found in multiple accounts, they will have edge with other emails from all these multiple accounts as well. The following diagram will help better visualize the scenario (In image, A is input list, Pi denotes person name of an account and Ei denotes emails) -
		from collections import defaultdict

		# DFS
		# class Solution:
		#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
		self.graph = defaultdict(set)
		self.visited = set()

		for account in accounts:
			# build adjacency list, add edge between first and the rest
			first = account[1]
			for i in range(2, len(account)):
				self.graph[first].add(account[i])
				self.graph[account[i]].add(first)

		# traverse to get components
		res = []
		for account in accounts:
			name = account[0]
			first = account[1]

			if first not in self.visited:
				merged_list = []
				self.dfs(merged_list, first)
				res.append([name] + sorted(merged_list))

		return res

	def dfs(self, merged, node):
		self.visited.add(node)
		merged.append(node)

		for neighbor in self.graph[node]:
			if neighbor not in self.visited:
				self.dfs(merged, neighbor)
