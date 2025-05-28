class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {')':'(','}':'{', ']':'['}
        for c in s:
            if c in mp: 
                top = st.pop() if st else '#'
                if mp[c] != top: return False
            else: st.append(c)
        return not st