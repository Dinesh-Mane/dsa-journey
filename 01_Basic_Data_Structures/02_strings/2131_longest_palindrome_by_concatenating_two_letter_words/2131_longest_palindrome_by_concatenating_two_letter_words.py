class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mp = [[0]*26 for i in range(26)]
        res = 0
        for w in words:
            a,b = ord(w[0])-ord('a'), ord(w[1])-ord('a')
            if mp[b][a]:
                res += 4
                mp[b][a]-=1
            else: mp[a][b]+=1
        for i in range(26):
            if mp[i][i]:
                res += 2
                break
        return res