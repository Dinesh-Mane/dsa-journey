from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        b = [[] for _ in range(len(nums)+1)]
        for x, f in c.items():
            b[f].append(x)
        res = []
        for i in range(len(b)-1, 0, -1):
            for x in b[i]:
                res.append(x)
                if len(res) == k:
                    return res