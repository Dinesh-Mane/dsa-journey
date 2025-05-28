# [344. Reverse String](https://leetcode.com/problems/reverse-string/description/)

## Problem Statement
Given a character array `s`, reverse the array in-place (i.e. without using extra memory).  
You must do this by modifying the input array directly with `O(1)` extra memory.

**Example**
```python
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```
```python
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Possible Solutions – Brute Force to Optimized
## 1) Brute Force – Using Extra Space (O(n) time, O(n) space)
**Idea:**  
1. Create a new array, reverse `s` into it, then copy back.
2. Not allowed as per constraints (not in-place).

**In-place? -> No**
```python
temp = s[::-1]   # reverse using slicing
for i in range(len(s)):
  s[i] = temp[i]
```
> Not acceptable in interviews or contests (breaks O(1) space rule)

## 2) Stack-based Reversal (O(n) Time, O(n) Space)
**In-place? -> No**
```python
st = list(s)
for i in range(len(s)):
  s[i] = st.pop()
```
> Educational, helps learn stack behavior. But not O(1) space → ❌ rejected.


## 3) Recursion (Time: O(n), Space: O(n) due to call stack)
Recursively swap outer elements, shrink the problem

**In-place? -> Yes**
```python
def helper(left, right):
  if left >= right: return
  s[left], s[right] = s[right], s[left]
  helper(left + 1, right - 1)
    
helper(0, len(s) - 1)
```
> Uses call stack → not truly O(1) space → not ideal for large input.

## 4) Built-in Python reverse – O(n) time, O(1) space but returns a new object
**In-place? -> Yes**
```python
s[:] = s[::-1]
```
> Works in Python, but may be rejected in stricter environments or interviews because it's too high-level.

## 5) Best & Optimal – Two-Pointer In-Place Swap (O(n) time, O(1) space)
**In-place? -> Yes**
```python
left, right = 0, len(s) - 1
while left < right:
  s[left], s[right] = s[right], s[left]  # swap
  left += 1
  right -= 1
```


# Summary
| Approach         | Time Complexity | Space Complexity | In-place? | Interview Worthy? |
| ---------------- | --------------- | ---------------- | --------- | ----------------- |
| Brute-force copy | O(n)            | O(n)             | ❌         | ❌                 |
| Stack reversal   | O(n)            | O(n)             | ❌         | ❌                 |
| Recursion        | O(n)            | O(n) (stack)     | ✅         | ❌                 |
| Built-in slicing | O(n)            | O(1)\*           | ✅ (sorta) | ❌ (Too Pythonic)  |
| Two-pointer swap | O(n)            | O(1)             | ✅         | ✅✅✅ (Best!)       |