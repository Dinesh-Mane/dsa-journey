class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(l,r):
            while l<r:
                s1[l], s1[r] = s1[r], s1[l]
                l+=1
                r-=1
        l=0
        s1 = list(s)
        for r in range(len(s1)):
            if s1[r] == ' ':
                reverse(l,r-1)
                l = r+1
        reverse(l, len(s1)-1) 
        return ''.join(s1)
