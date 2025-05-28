class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, v in enumerate(nums):
            r = target - v
            if r in hash: return [hash[r], i]
            hash[v] = i