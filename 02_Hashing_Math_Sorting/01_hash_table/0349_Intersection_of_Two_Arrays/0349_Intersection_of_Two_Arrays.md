# [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/description/)

## Problem Statement
You are given two integer arrays `nums1` and `nums2`. Your task is to return an array of unique elements that appear in both arrays.
- The result should not contain duplicates.
- The order of output does not matter.

**Example**
```python
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```
```python
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force (O(n × m) Time, O(1) Space)
**Idea:** Loop through each element in nums1, and for each, check if it exists in nums2. Avoid duplicates by checking if it already exists in the result.

```python
res = []
for i in nums1:
  if i in nums2 and i not in res: res.append(i)
return result
```
## 2) Sorting + Two Pointers (O(n log n + m log m) Time, O(1) Space)
**Idea:** 
1. Sort both arrays.
2. Use two pointers to iterate and find common elements.
3. Avoid duplicates by checking the last added value

```python
nums1.sort()
nums2.sort()
i = j = 0
result = []

while i < len(nums1) and j < len(nums2):
  if nums1[i] == nums2[j]:
    if not result or result[-1] != nums1[i]: result.append(nums1[i])
    i += 1
    j += 1
  elif nums1[i] < nums2[j]: i += 1
  else: j += 1
return result
```
Compact : 
```python
nums1.sort(); nums2.sort()
i = j = 0; res = []

while i < len(nums1) and j < len(nums2):
  if nums1[i] == nums2[j]:
    if not res or res[-1] != nums1[i]: res.append(nums1[i])
    i += 1; j += 1
  elif nums1[i] < nums2[j]: i += 1
  else: j += 1
return res
```

## 3) HashSet (O(n + m) Time, O(n) Space)
**Idea:**  
1. Store elements from `nums1` in a set.
2. Loop through `nums2` and add elements to result if they are in the set.
3. Use a second set for the result to ensure uniqueness.

```python
s = set(nums1)
res = set()

for n in nums2:
  if n in s: res.add(n)

return list(res)
```
> This is a fast and clean approach for coding interviews.

## 4) Using Built-in Python Set Operations (O(n + m) time, O(n) space)
**Idea:** Use Python’s built-in set intersection operator (`&`) to get common unique values.

```python
return list(set(nums1) & set(nums2))
```

## Jr aplyala union kadhaycha asel two lists cha:
**Set Union in Python**: To find the union of two arrays (i.e., all unique elements present in either array), you can use:

### 1. Using union operator |
```python
return list(set(nums1) | set(nums2))
```
### 2. Using set.union() method
```python
return list(set(nums1).union(set(nums2)))
```
Both versions will give the same result – a list of all unique elements from both arrays.