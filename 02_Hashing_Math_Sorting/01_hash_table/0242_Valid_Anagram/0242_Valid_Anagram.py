class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False

        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c,0)+1
        
        for c in t:
            if c not in cnt or cnt[c] == 0: return False
            cnt[c]-=1
        return True
