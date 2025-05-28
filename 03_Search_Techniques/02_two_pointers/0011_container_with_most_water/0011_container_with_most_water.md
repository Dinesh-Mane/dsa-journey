# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)

## Problem Statement
Given n non-negative integers, each representing a vertical line on the x-axis with height height[i],
> Find two lines such that they form a container that holds the most water.

Each vertical line is at coordinate i, and container's area =
> min(height[i], height[j]) × (j - i)  
 
**Example**
```python
Input: prices = [7,1,5,3,6,4]
Output: 7

Explanation: 
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Lines at index 1 and 8 (height=8 and 7) give area = 7 * (8 - 1) = 49
```
```python
Input: height = [1,1]
Output: 1
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Try all pairs (Time: O(n^2), Space: O(1))  
Idea: सगळ्या possible pairs (i, j) check karaycha ani प्रत्येक time la `max area` track karaycha  
```python
max_area = 0
n = len(height)
for i in range(n):
  for j in range(i+1, n):
    curr_area = min(height[i], height[j]) * (j - i)
    max_area = max(max_area, curr_area)
return max_area
```

## 2) Optimized - Two-Pointer Technique (O(n) time, O(1) space)  
**Idea:** Start with two pointers: one at the start (`left`) and one at the end (`right`).  
Calculate area between them, and move the **pointer pointing to the shorter line inward.** and keep track of `max_area`

> Why move the shorter line?  
> Because the height is limiting — moving the taller one does not help increase area, but moving the shorter might.  
```python
left, right = 0, len(height) - 1
max_area = 0
while left < right:
  curr_area = min(height[left], height[right]) * (right - left)
  max_area = max(max_area, curr_area)
  if height[left] < height[right]: left += 1
  else: right -= 1
return max_area
```
