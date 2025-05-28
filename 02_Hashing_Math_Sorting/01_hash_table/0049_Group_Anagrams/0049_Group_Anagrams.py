class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for w in strs:
            cnt = [0]*26
            for c in w:
                cnt[ord(c)-ord('a')]+=1
            key = tuple(cnt)
            res[key].append(w)
        return list(res.values())