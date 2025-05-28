class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefix_sum = 0
        rem_cnt = {0: 1}
        for n in nums:
            prefix_sum += n
            rem = prefix_sum % k
            cnt += rem_cnt.get(rem,0)
            rem_cnt[rem] = rem_cnt.get(rem,0) + 1
        return cnt