class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #         digit_logs = []
        #         letter_logs = []
        #         for log in logs:
        #             identifier = log.split()[0]

        #             # Extracting the digit-logs
        #             if log.split()[1].isdigit():
        #                 digit_logs.append(log)
        #             else:
        #                 letter_logs.append(log)

        #         # Sorting the letter-logs
        #         letter_logs.sort(key = lambda x: [x.split()[1:], x.split()[0]])
        #         return letter_logs + digit_logs

        # Time: O(M.N log N) where M is the maximum length of single log
        # Space: O(M. N) 
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1,)

        return sorted(logs, key=get_key)
