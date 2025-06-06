class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1
        curr = 0
        for i, x in enumerate(nums):
            curr += diff[i]
            if curr < x:
                return False
        return True