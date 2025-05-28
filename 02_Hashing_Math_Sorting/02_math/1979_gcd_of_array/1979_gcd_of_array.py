class Solution:
    def gcd(a,b):
        while b:
            a,b = b, a%b
        return a

    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))