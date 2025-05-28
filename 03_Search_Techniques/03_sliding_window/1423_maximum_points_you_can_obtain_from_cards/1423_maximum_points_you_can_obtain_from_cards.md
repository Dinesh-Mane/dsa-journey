# [1423. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/)

## Problem Statement
You are given an integer array cardPoints and an integer k. You can pick exactly k cards either from the beginning or the end of the array.  
Your goal: Maximize the sum of points from the selected k cards.  

**Example**
```python
Input: cardPoints = [1,2,3,4,5,6,1], k = 3  
Output: 12  
Explanation: Pick the last 2 cards (6,1) and the first 1 card (1), total = 1 + 6 + 1 = 8 is less than 1 + 2 + 3 = 6, but 1 + 6 + 5 = 12 is max.
```
```python
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
```
```python
Input: cardPoints = [2,2,2], k = 2
Output: 4
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Try All combinations – TLE (Time: O(k²), Space: O(1))  
Try all combinations of taking cards from front and back.  
> **Dry Run Idea:** Try 0 from left, k from right; then 1 from left, k-1 from right ... until k from left, 0 from right.  

```python
n = len(cardPoints)
max_sum = 0
for i in range(k + 1):  # i cards from front, k-i from end
  left = sum(cardPoints[:i])
  right = sum(cardPoints[n - (k - i):])
  max_sum = max(max_sum, left + right)
return max_sum
```
> ❌ No, time-consuming

## 2) Prefix + Suffix (Time: O(k), Space: O(k))  
Store left prefix sums and right suffix sums, then try all splits.  
```python
left_sum = [0] * (k + 1)
right_sum = [0] * (k + 1)
    
for i in range(1, k+1):
  left_sum[i] = left_sum[i - 1] + cardPoints[i - 1]
  right_sum[i] = right_sum[i - 1] + cardPoints[-i]

max_sum = 0
for i in range(k + 1):
  max_sum = max(max_sum, left_sum[i] + right_sum[k - i])
return max_sum
```
> ✅ Decent, but uses extra space
## 3) Two Pointers (Greedy Sliding Concept) (Time: O(k), Space: O(1))  
Use two pointers – one from left and one from right. Start with left k cards. Then replace one-by-one from right side and adjust the score.
```python
curr_sum = sum(cardPoints[:k])
max_score = curr_sum
  
for i in range(1, k + 1):
  curr_sum = curr_sum - cardPoints[k - i] + cardPoints[-i]
  max_score = max(max_score, curr_sum)
    
return max_score
```
> ✅ Good, but limited to k operations
## 4) Optimized - Sliding Window (O(n) time, O(1) space)  
**Logic:**  
Instead of selecting k cards, we remove (n - k) continuous cards from the middle.  
Then maximize sum = totalSum - sum(removed window)  
```python
n = len(cardPoints)
window_size = n - k
total = sum(cardPoints)
window_sum = sum(cardPoints[:window_size])   # Step 1: Compute sum of first window
min_window_sum = window_sum
    
for i in range(window_size, n):   # Step 2: Slide the window
  window_sum += cardPoints[i] - cardPoints[i - window_size]
  min_window_sum = min(min_window_sum, window_sum)
return total - min_window_sum
```
> ✅✅ Best for large input sizes