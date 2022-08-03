from typing import *


class Solution:
	def numUniqueEmails(self, emails: List[str]) -> int:
		# approach1: set + string clean for each email
		email_set = set()

		for email in emails:
			local_name, domain_name = email.split('@')

			# split the local by '+' and replace all '.' with ''
			local_name = local_name.split('+')[0].replace('.', '')

			# concatenate the local, '@' and domain name
			email_set.add(local_name + '@' + domain_name)

		return len(email_set)

# time: O(N*M), N IS THE NUMBER OF EMAILS, M IS THE AVERAGE LENGTH OF AN EMAIL
# SPACE: O(N*M). IN THE WORST CASE, ALL EMAILS ARE UNIQUE AND WE HAVE TO STORE ALL OF THEM
