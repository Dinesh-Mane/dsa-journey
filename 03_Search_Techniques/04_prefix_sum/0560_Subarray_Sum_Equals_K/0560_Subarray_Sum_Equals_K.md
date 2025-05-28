# [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/)

## Problem Statement
Given an integer array `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.  

**Example**
```python
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: [1,1] appears twice
```
```python
Input: nums = [1,2,3], k = 3
Output: 2
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Double Loop with Running Sum - (Time: O(n²), Space: O(1))  
**Logic:**
> Try all possible subarrays and check their sum.  
> TLE for large input

```python
count = 0
for i in range(len(nums)):
  sum = 0
  for j in range(i, len(nums)):
    sum += nums[j]
    if sum == k: count += 1
return count
```

## 2) Optimized - Prefix Sum + HashMap (O(n) time, O(n) space)  
If we define `prefix_sum[i]` as the sum of `nums[0...i]`,  
then if `prefix_sum[j] - prefix_sum[i] == k`,  
that means subarray `nums[i+1...j]` sums to `k`.  
So we store `prefix_sum` frequencies in a hashmap to check how many times `current_sum - k` has occurred.  

**Steps:**  
> Maintain a running sum  
> Use a hash map to store how many times a prefix sum has occurred  

```python
count = 0
psum = 0
mapp = {0: 1}  # to count subarrays starting at index 0

for n in nums:
  psum += n
  if psum - k in mapp: count += mapp[psum - k]
  mapp[psum] = mapp.get(psum, 0) + 1
return count
```

## OR
🧠 Idea:  
> Traverse the array and compute cumulative prefix_sum.  
> At each step, check if (prefix_sum - k) is already in the hashmap.  
> Keep adding prefix_sum to the hashmap for future reference.  

```python
from collections import defaultdict
mapp = defaultdict(int)
mapp[0] = 1  # for subarrays starting from index 0

count = 0
psum = 0

for n in nums:
  psum += n
  count += mapp[psum - k]
  mapp[psum] += 1
return count
```
