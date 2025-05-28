class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        seen = set()
        l=0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            mx = max(mx, r-l+1)
        return mx