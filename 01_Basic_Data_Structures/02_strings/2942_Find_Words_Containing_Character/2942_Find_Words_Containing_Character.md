# [344. Reverse String](https://leetcode.com/problems/reverse-string/description/)

## Problem Statement
You are given a 0-indexed array of strings `words` and a character `x`  
Your task is to: Return a list of all indices `i` such that `x` is present in `words[i]`

**Example**
```python
Input: words = ["leet", "code"], x = "e"
Output: [0, 1]
```
```python
Input: words = ["abc", "bcd", "aaaa", "cbc"], x = "a"
Output: [0, 2]
```

## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach (O(n * m) time, O(1) space)
**Idea:** For each word in the list, scan every character. If x exists in that word, store its index.

```python
res = []
for i in range(len(words)):
  for c in words[i]:
    if c == x:
      res.append(i)
      break
return res
```

## 2) Simplified Pythonic Approach (O(n * m) Time, O(1) Space)

```python
return [i for i, word in enumerate(words) if x in word]
```
if you want to stop the seraching as soon as wee found the match
```python
return [i for i, word in enumerate(words) if any(ch == x for ch in word)]
```
OR
```python
res = []
for i, word in enumerate(words):
  found = False
  for ch in word:
    if ch == x:
      res.append(i)
      break  # early exit
return res
```
> This avoids scanning full word if x is at the beginning.
> Time Complexity: Best case: `O(n)`, Worst case: `O(n * m)`


# Summary
| Approach                  | Time      | Space | Notes                             |
| ------------------------- | --------- | ----- | --------------------------------- |
| Brute Force (nested loop) | O(n \* m) | O(1)  | Clear logic but verbose           |
| Pythonic `in` operator    | O(n \* m) | O(1)  | Best in interviews (short, clean) |
| `any()` with generator    | O(n \* m) | O(1)  | Short, early exit possible        |
| Manual early exit loop    | O(n \* m) | O(1)  | Control over iteration steps      |