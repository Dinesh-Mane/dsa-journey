# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

## Problem Statement
Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and false otherwise.
> An anagram is a word formed by rearranging the letters of another, using all the original letters exactly once.

**Example**
```python
Input: s = "anagram", t = "nagaram"
Output: True
```
```python
Input: s = "rat", t = "car"
Output: False
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force – Character Matching with Visited Flags (O(n²) Time, O(n) Space)
**Idea:** For each character in `s`, search for a matching character in `t` that hasn't been matched yet. Use a visited array to keep track of matched characters in `t`

```python
if len(s) != len(t): return False

visited = [False] * len(t)
for i in range(len(s)):
  found = False
  for j in range(len(t)):
    if s[i] == t[j] and not visited[j]:
    visited[j] = True
    found = True
    break
if not found:
  return False
return True
```
## 2) Sorting Both Strings and Comparing (O(n log n) Time, O(n) Space)
**Idea:** Sort both strings and compare them. If they are equal, they are anagrams.   

```python
return sorted(s) == sorted(t)
```

## 3) Using Hash Maps to Count Character Frequencies (O(n) Time, O(n) Space)
**Idea:** Count the frequency of each character in both strings using hash maps and compare the two maps.
```python
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
  return Counter(s) == Counter(t)
```

## 4) Using a Single Hash Map (O(n) Time, O(n) Space)
**Idea:** Count the frequency of each character in s. Then, decrement the count for each character in t. If any count goes below zero or a character is not found, return False.

```python
if len(s) != len(t): return False

cnt = {}
for c in s:
 cnt[c] = cnt.get(c, 0) + 1

 for c in t:
  if c not in cnt or cnt[c] == 0: return False
  cnt[c] -= 1

return True
```

## 5) Using Fixed-Size Array for Lowercase Letters (O(n) Time, O(1) Space)
**Idea:** Since the strings contain only lowercase English letters, use an array of size 26 to count character frequencies.

```python
if len(s) != len(t): return False

cnt = [0] * 26
for i in range(len(s)):
  cnt[ord(s[i]) - ord('a')] += 1
  cnt[ord(t[i]) - ord('a')] -= 1

return all(x == 0 for x in cnt)
```

Note: For coding interviews, the fixed-size array approach is highly efficient when dealing with lowercase English letters. If the input may contain Unicode characters or mixed cases, using hash maps is a more general solution.