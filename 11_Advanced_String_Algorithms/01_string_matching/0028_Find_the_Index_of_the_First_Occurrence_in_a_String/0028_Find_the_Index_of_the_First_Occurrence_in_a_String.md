# [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)

## Problem Statement
You're given two strings:  
1. `haystack` – the main string
2. `needle` – the substring you want to find

**Task:**  
Return the index of the first occurrence of `needle` in `haystack`  
If `needle` is not found, return `-1`.  

Note: `needle` can be an empty string → In that case, return `0`.

**Example**
```python
Input: haystack = "sadbutsad", needle = "sad"
Output: 0  # because "sad" starts at index 0

Input: haystack = "leetcode", needle = "leeto"
Output: -1  # not found

Input: haystack = "hello", needle = ""
Output: 0  # empty string is always found at start
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force – Compare Every Substring (O((h−n+1) * n) time, O(1) space)
**Idea:** Try every possible starting index `i` in `haystack` and compare the substring `haystack[i:i+n]` to `needle`. If match → return `i`.

```python
h, n = len(haystack), len(needle)
for i in range(h - n + 1):
  if haystack[i:i + n] == needle: return i
return -1
```

## 2) Manual Char-by-Char Match (O((h-n+1) * n) Time, O(1) Space)
**Idea:** Instead of slicing (which creates substrings), compare characters one by one.
> Faster in practice, especially in C/C++/Java.

```python
h, n = len(haystack), len(needle)
for i in range(h - n + 1):
  match = True
  for j in range(n):
    if haystack[i + j] != needle[j]:
      match = False
      break
    if match: return i
return -1
```


## 3) Built-in `find()` or `index()` (Time: O((h−n+1) * n), Space: O(1))
Use regular expressions to remove non-alphanumeric characters

```python
return haystack.find(needle)
```
```python
try:
  return haystack.index(needle)
except ValueError:
  return -1
```
> Easy and fast but Not accepted in manual coding interviews – they expect you to implement the logic

## 4) Knuth-Morris-Pratt (KMP) Algorithm – Optimal Pattern Matching  (Time: O(h + n), Space: O(n))
**Idea:**  
- Preprocess `needle` into a prefix table (`lps`) that tells us how much to skip if there's a mismatch.
- Then scan through `haystack` and match using this table.

> Great for large strings and repeated patterns.

```python
def strStr(haystack: str, needle: str) -> int:
  def buildLPS(pattern):
    lps = [0] * len(pattern)
    length = 0  # length of previous longest prefix suffix
    i = 1
    while i < len(pattern):
      if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
      else:
        if length != 0: length = lps[length - 1]  # fallback
        else:
          lps[i] = 0
          i += 1
    return lps

  if not needle: return 0
  lps = buildLPS(needle)
  i = j = 0  # i for haystack, j for needle

  while i < len(haystack):
    if haystack[i] == needle[j]:
      i += 1
      j += 1
      if j == len(needle): return i - j
      else:
        if j != 0: j = lps[j - 1]  # fallback
        else: i += 1
  return -1
```