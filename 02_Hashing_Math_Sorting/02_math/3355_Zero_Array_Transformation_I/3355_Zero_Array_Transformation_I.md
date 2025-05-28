# [3355. Zero Array Transformation I](https://leetcode.com/problems/zero-array-transformation-i/description/?envType=daily-question&envId=2025-05-20)

## Problem Statement
You are given:
- `nums`: an integer array of size `n`
- `queries`: list of intervals `[li, ri]`

For each query, you can choose any subset of indices in range `[li, ri]` and decrease their values by 1.  
Return True if, after applying all queries sequentially, you can make every element in `nums` equal to 0 (i.e., form a "Zero Array").  

### Core Insight
Each element of `nums[i]` must be decremented exactly `nums[i]` times total across queries. But:
- We can only decrement inside allowed intervals.
- So, each index `i` must appear in at least `nums[i]` different query ranges.

## Reformulated Problem
For every i, check:
```python
number of queries where li ≤ i ≤ ri >= nums[i]
```
If this is true for all indices i, the transformation is possible.

**Example**
```python
Input: nums = [1,0,1], queries = [[0,2]]
Output: true
Explanation:
For i = 0:
- Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
- The array will become [0, 0, 0], which is a Zero Array.
```
```python
Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]
Output: false
Explanation:
For i = 0:
- Select the subset of indices as [1, 2, 3] and decrement the values at these indices by 1.
- The array will become [4, 2, 1, 0].
For i = 1:
- Select the subset of indices as [0, 1, 2] and decrement the values at these indices by 1.
- The array will become [3, 1, 0, 0], which is not a Zero Array.
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force (O(n * q)) – TLE for large input
Idea: Loop through every query and mark how many times each index is covered.
```python
n = len(nums)
count = [0] * n  # to count how many times each index is covered
for l, r in queries:
  for i in range(l, r + 1):
    count[i] += 1

for i in range(n):
  if count[i] < nums[i]: return False
return True
```
## 2) Difference Array (Prefix Sum Trick) – O(n + q)
**Idea:** Instead of updating every index in each query, use prefix sum style range increments.

Step-by-step:
- Use a diff array.
- For query [l, r], do:
```python
diff[l] += 1
diff[r+1] -= 1
```
- Build the actual coverage array using prefix sum over diff.

```python
n = len(nums)
diff = [0] * (n + 1)

for l, r in queries:
  diff[l] += 1
  if r + 1 < len(diff): diff[r + 1] -= 1

  coverage = [0] * n
  coverage[0] = diff[0]

for i in range(1, n):
  coverage[i] = coverage[i - 1] + diff[i]

for i in range(n):
  if coverage[i] < nums[i]: return False
return True
```

## 3) One-Liner Variant (Optimized Space) – Still O(n + q)

**Idea:** Use same logic but with compact prefix addition and check.
```python
n = len(nums)
diff = [0] * (n + 1)

for l, r in queries:
  diff[l] += 1
  if r + 1 < n: diff[r + 1] -= 1

curr = 0
for i in range(n):
  curr += diff[i]
  if curr < nums[i]:return False
return True
```
OR
```python
diff = [0] * (len(nums) + 1)
for l, r in queries:
  diff[l] += 1
  diff[r + 1] -= 1
curr = 0
for i, x in enumerate(nums):
  curr += diff[i]
  if curr < x: return False
return True
```