class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        freq = defaultdict(int)
        for n in nums:
            cnt += freq[n-k] + freq[n+k]
            freq[n] += 1
        return cnt