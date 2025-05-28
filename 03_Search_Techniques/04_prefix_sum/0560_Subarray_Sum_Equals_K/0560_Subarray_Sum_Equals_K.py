class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        psum = 0
        mapp ={0:1}
        for n in nums:
            psum += n
            if psum - k in mapp: cnt += mapp[psum-k]
            mapp[psum] = mapp.get(psum,0)+1
        return cnt