class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1,num2=0,0
        total_sum = n*(n+1)//2
        k = n//m
        div_sum = (k*(2*m + (k-1)*m))//2
        return total_sum - 2*div_sum