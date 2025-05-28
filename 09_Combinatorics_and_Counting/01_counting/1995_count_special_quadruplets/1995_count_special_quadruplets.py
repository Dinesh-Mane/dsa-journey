class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        freq = defaultdict(int)
        for b in range(n-3, -1, -1):
            for d in range(b+2, n):
                diff = nums[d] - nums[b+1]
                freq[diff] += 1
            for a in range(b):
                total = nums[a] + nums[b]
                count += freq[total]
        return count