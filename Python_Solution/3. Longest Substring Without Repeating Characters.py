class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        max_len = 0
        start = 0
        for idx in range(len(s)):
            if s[idx] in seen:
                start = max(start, seen[s[idx]] + 1)
            seen[s[idx]] = idx
            max_len = max(max_len, idx - start + 1)
        return max_len
