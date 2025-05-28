# [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/)

## Problem Statement
Given an integer array nums of length n where all the integers are in the range [1, n], some elements appear twice and others appear once.  
Return all the elements that appear twice in any order.   
> n == nums.length  
> Each integer appears once or twice only  
> Use O(n) time and preferably O(1) extra space (excluding output)    

**Example**
```python
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```
```python
Input: nums = [1,1,2]
Output: [1]
```

## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Nested Loop (Time: O(n^2), Space: O(n))
> For every element, check how many times it appears using count.  
> Not efficient, but works for small input.  
> Time: O(n²) → as `nums.count(i)` is O(n)  

```python
res = []
for n in nums:
    if nums.count(n) == 2 and n not in res: res.append(n)
return res
```
## 2) Hash Map / Set (Extra Space) (Time: O(n), Space: O(n))
Use a set to track seen elements. If an element is already in the set, it is a duplicate.  
```python
seen = set()
res = []
for n in nums:
    if num in seen: res.append(n)
    else: seen.add(n)
return res
```
### OR
Store frequency of each number using a dictionary.  
```python
freq = {}
res = []
for n in nums:
    freq[n] = freq.get(n, 0) + 1
for n, cnt in freq.items():
    if cnt == 2: res.append(n)
return res
```
### OR - We can Directly use built-in function
> Python चा `collections.Counter()` वापर.  
> Count == 2 असेल तर त्या key ला result मध्ये टाक.

```python
from collections import Counter

def findDuplicates(nums):
    freq = Counter(nums)
    return [n for n, cnt in freq.items() if cnt == 2]
```

## 3) Optimized - index marking technique / In-place Sign Flipping - (O(n) time, O(1) extra space)
Given की:  
> `1 <= nums[i] <= n`  
> Since `nums[i]` ranges from 1 to n, we can use `index = abs(num) - 1` and flip the sign at that index.
> If the value at that index is already negative, it means we've seen it before = duplicate.
> आपण original array ला modify करू शकतो.  
> त्यामुळे आपण index marking technique वापरू.

Idea:
> प्रत्येक number `num`, त्याचं absolute value घ्या ➔ `index = abs(num) - 1 `  
> त्या index च्या value ला negative करा.  
> जर already negative असेल ➔ मग तो number duplicate आहे.  

```python
res = []
for n in nums:
    index = abs(n) - 1
    if nums[index] < 0: res.append(abs(n))
    else: nums[index] = -nums[index]
return res
```
