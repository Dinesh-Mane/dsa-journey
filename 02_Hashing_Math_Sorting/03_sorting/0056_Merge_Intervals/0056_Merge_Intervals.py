class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort()
        i = 0
        for j in range(1, len(a)):
            if a[j][0] <= a[i][1]:
                a[i][1] = max(a[i][1], a[j][1])
            else:
                i += 1
                a[i] = a[j]
        return a[:i+1]