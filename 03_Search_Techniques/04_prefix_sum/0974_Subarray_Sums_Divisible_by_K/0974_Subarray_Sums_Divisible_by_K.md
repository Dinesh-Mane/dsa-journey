# [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/description/)

## Problem Statement
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.  
> A subarray is a contiguous part of an array.  

दिलेल्या array मधून किती subarrays आहेत ज्यांचा sum पूर्णपणे `k` ने भाग जातो (i.e., `sum % k == 0`) हे शोधायचं आहे.  

**Example**
```python
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```
```python
Input: nums = [5], k = 9
Output: 0
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Prefix Sums (Time: O(n²), Space: O(1))  
Idea:   
Check sum of all subarrays, and count if divisible by k.    
```python
cnt = 0
for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total += nums[j]
        if total % k == 0: cnt += 1
return cnt
```
## 2) Optimized - Prefix Sum + HashMap (O(n) time, O(k) space)  
**Logic:**  
If the difference between two prefix sums is divisible by k, the subarray between them is divisible by k.  
> If `(prefixSum[j] - prefixSum[i]) % k == 0`, then `prefixSum[j] % k == prefixSum[i] % k`  
> जर दोन prefix sums ला एकच remainder (modulo) मिळत असेल, तर त्यांच्यातील subarray `k` ने divisible असतो.

We use the idea of remainders: If (prefix_sum % k) has been seen before, that means there is a subarray ending at this index that is divisible by k.  

```python
cnt = 0
prefix_sum = 0
rem_cnt = {0: 1}   # remainder 0 already exists once

for n in nums:
  prefix_sum += n
  rem = prefix_sum % k
  if rem < 0: rem = (rem + k) % k   # Handle negative remainders
  cnt += rem_cnt.get(rem, 0)   # जर हाच remainder आधी आलेला असेल तर त्याच्या count एवढे subarrays आहेत
  rem_cnt[rem] = rem_cnt.get(rem, 0) + 1   # ह्या rem ची count वाढवा
return cnt
```