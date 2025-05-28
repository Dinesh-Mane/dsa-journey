class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        prev = -1
        for i in s:
            if i.isdigit():
                if int(i)<=prev: return False
                prev = int(i)
        return True