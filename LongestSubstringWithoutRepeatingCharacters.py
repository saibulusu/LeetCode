class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        start = 0
        dict = {}
        for i in range(0, len(s)):
            if s[i] in dict:
                res = max(i - start, res)
                start = max(dict[s[i]] + 1, start)
            dict[s[i]] = i
        res = max(len(s) - start, res)
        return res
