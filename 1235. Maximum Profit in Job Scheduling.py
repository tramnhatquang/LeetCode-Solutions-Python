class Solution:

	def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
		# def jobScheduling(startTime, endTime, profit):
		"""
The first step is to sort the jobs by their end times. This is because if we have two jobs i and j with i < j, and endTime[i] > endTime[j], then it is always better to schedule job j instead of job i, since it ends earlier and allows us to schedule more jobs in total.

After sorting the jobs, we define dp[i] to be the maximum profit we can obtain by scheduling jobs from 0 to i such that the i-th job is included. We will compute dp[i] for each i in turn, starting from 0 and ending at n-1.

To compute dp[i], we consider two cases:

We don't include the i-th job. In this case, dp[i] = dp[i-1], since we can simply copy the maximum profit we obtained by scheduling jobs from 0 to i-1.

We include the i-th job. In this case, we need to find the last job j that ends before the i-th job starts, such that jobs from 0 to j do not overlap with the i-th job. We can do this using binary search on the sorted jobs. Specifically, we can find the largest j such that endTime[j] <= startTime[i]. Then, dp[i] = max(dp[i-1], dp[j] + profit[i]), since we either copy the maximum profit obtained by scheduling jobs from 0 to i-1, or we add the profit from the i-th job and the maximum profit obtained by scheduling jobs from 0 to j.

The final answer is given by dp[n-1], which is the maximum profit we can obtain by scheduling jobs from 0 to n-1.

The time complexity of this solution is dominated by the sorting step, which takes O(n log n) time. The binary search and the computation of dp[i] for each i take O(log n) and O(1) time per job, respectively, so the overall time complexity is O(n log n).
		"""
		n = len(startTime)
		jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
		dp = [0] * n
		dp[0] = jobs[0][2]

		for i in range(1, n):
			start_i, end_i, profit_i = jobs[i]
			dp[i] = max(dp[i - 1], profit_i)  # do not include the i-th job

			j = i - 1
			while j >= 0 and jobs[j][1] > start_i:
				j -= 1
			if j >= 0:
				dp[i] = max(dp[i], dp[j] + profit_i)  # we include the i-th job

		return dp[n - 1]
