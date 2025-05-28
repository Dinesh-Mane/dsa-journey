# [75. Sort Colors](https://leetcode.com/problems/sort-colors/description/)

## Problem Statement
एक integer array `nums` दिला आहे ज्यात फक्त 3 values आहेत: `0` (red), `1` (white), आणि `2` (blue).  
Goal: ह्या colors ना अशी sort कर की `0` (red) सर्वात आधी, मग `1` (white), मग `2` (blue) येतील.

> Constraint:
> In-place sorting करायची आहे. म्हणजे extra space वापरायचा नाही.


**Example**
```python
Input:  nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
```
```python
Input: nums = [2, 0, 1]
Output: [0, 1, 2]
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Sort using built-in function (O(n log n) time, O(1) space (if in-place))
```python
nums.sort()  # Default sort ascending - 0s first, then 1s, then 2s
```
## 2) Counting Sort (O(n) time, O(1) space) 
> 1st pass – Count how many 0s, 1s, and 2s  
> 2nd pass – Overwrite the array accordingly  
```python
cnt = [0]*3 #count = [0, 0, 0]  # count[0] = no. of 0s, count[1] = no. of 1s, count[2] = no. of 2s
for n in nums: cnt[n] += 1
i = 0
for color in range(3):
    for _ in range(count[color]):
        nums[i] = color
        i += 1

```
## 3) Optimized - Dutch National Flag Algorithm (O(n) Time, O(1) Space)  
> Idea: Use 3 pointers – low, mid, and high  
> low – boundary for 0  
> high – boundary for 2  
> mid – current element

> Logic:  
> nums[mid] == 0 → swap(nums[low], nums[mid]), low++, mid++  
> nums[mid] == 1 → mid++  
> nums[mid] == 2 → swap(nums[mid], nums[high]), high--  

```python
low = 0                #starting la thevu
mid = 0                #curr element, yacha use karun travers karu
high = len(nums) - 1   #shevati thevu
while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1: mid += 1
    else:  # nums[mid] == 2
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
```
> ❗Limitations of NFA:  
> Only applicable when there are exactly 3 distinct values (like 0,1,2)  
> For more than 3 categories, use Counting Sort or Bucket Sort  