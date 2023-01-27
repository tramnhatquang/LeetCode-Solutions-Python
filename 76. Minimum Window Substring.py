class Solution:
    def minWindow(self, s: str, t: str) -> str:\
        # NOTICE: 
        # The t string can contain duplicates
        # The question is about find the minimum window substring whose chars and their frequencies are the same in the t string

        sLen, tLen = len(s), len(t)
        if tLen > sLen: # sanity check
            return ""

        # given that sLen, tLen >= 1, we do not need to check empty check
        t_counter = collections.Counter(t)
        left = 0
        # the number of required distinct keys 
        required = len(t_counter)
        satisfied = 0
        res, resLen = [-1, -1], float("infinity")
        window = collections.defaultdict(int)

        for right in range(sLen):
            # keep track only characters that appear in the check
            char = s[right]
            if char in t_counter:
                window[char] += 1
                if window[char] == t_counter[char]:
                    satisfied += 1
            
            # shrinking the window when statisfied == required
            while satisfied == required:
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    res = (left, right)
                if s[left] in t_counter:
                    window[s[left]] -= 1
                    if window[s[left]] < t_counter[s[left]]:
                        satisfied -= 1
                left += 1
        return s[res[0]: res[1] + 1]


