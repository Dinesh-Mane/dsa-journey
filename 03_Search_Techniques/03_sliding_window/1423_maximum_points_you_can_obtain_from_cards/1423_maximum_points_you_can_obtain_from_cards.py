class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        curr = sum(cardPoints[:k])
        maxi = curr
        for i in range(1, k+1):
            curr = curr - cardPoints[k-i] + cardPoints[-i]
            maxi = max(maxi, curr)
        return maxi