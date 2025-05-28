from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return ''.join(ch * freq for ch, freq in sorted(c.items(), key=lambda x: -x[1]))