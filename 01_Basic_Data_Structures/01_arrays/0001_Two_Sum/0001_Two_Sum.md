# [1. Two Sum](https://leetcode.com/problems/two-sum/description/)

## Problem Statement
Given an array of integers `nums[]` and an integer `target`, Return indices of the two numbers such that they add up to `target`.  
> You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Constraints:**  
Only one valid pair will exist.  
You can't use the same element twice (i.e., don’t reuse index).  
Return the indices, not the values.  

**Example**
```python
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
```python
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Try all pairs ( Time: O(n²), Space: O(1))  
Idea:   
Try every possible pair `(i, j)` and check if `nums[i] + nums[j] == target `
> प्रत्येक element साठी दुसरा element शोधायचा जो मिळून target देईल.

```python
for i in range(len(nums)):
  for j in range(i+1, len(nums)):
    if nums[i] + nums[j] == target: return [i, j]
```
## 2) Two-pass Hash Map Approach (O(n) time, O(n) space)  
Step 1: Store all elements with their indices in a hash map  
Step 2: Check for `target - current`   

```python
hash = {}
for i in range(len(nums)): hash[nums[i]] = i 
for i in range(len(nums)):
  r = target - nums[i]
  if r in hash and hash[r] != i: return [i, hash[r]]
```

## 3) Optimized - One-pass Hash Map Approach (O(n) time, O(n) space)  
**Idea:** एका pass मध्ये, प्रत्येक element साठी target - num चा complement आहे का hash map मध्ये ते check करतो. नसेल तर हा element hash map मध्ये ठेवतो  
```python
hash = {} #dictinary (v:i)
for i,v in enumerate(n): 
  r = t - v
  if r in hash: return [hash[r], i]
  else: hash[v] = i
```

## 4) Generalized kSum (Reusable for 2Sum, 3Sum, 4Sum...)
Idea:
> Write a recursive kSum function.  
> Reduce it down to 2Sum problem.  
> Reusable & scalable for k = 4, 5, etc.

```python
def fourSum(nums, target):
    def kSum(nums, target, k):
        res = []
        if not nums:
            return res

        # Early termination
        avg_val = target // k
        if avg_val < nums[0] or avg_val > nums[-1]:
            return res

        # Base case: 2Sum using two pointers
        if k == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

        return res

    nums.sort()
    return kSum(nums, target, 4)
```
