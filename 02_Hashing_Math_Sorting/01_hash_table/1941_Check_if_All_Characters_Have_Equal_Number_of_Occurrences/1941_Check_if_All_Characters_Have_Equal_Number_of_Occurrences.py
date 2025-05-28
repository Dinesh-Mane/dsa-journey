class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        count = 0
        for n in freq:
            if n:
                if count == 0: count = n
                elif n != count: return False
        return True