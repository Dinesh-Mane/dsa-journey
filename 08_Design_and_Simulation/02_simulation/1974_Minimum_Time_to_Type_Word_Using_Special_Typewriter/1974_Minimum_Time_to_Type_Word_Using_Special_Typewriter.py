class Solution:
    def minTimeToType(self, word: str) -> int:
        tt=0
        prev = 'a'
        for c in word:
            diff = abs(ord(c)-ord(prev)) 
            tt += min(diff, 26-diff) + 1
            prev = c
        return tt