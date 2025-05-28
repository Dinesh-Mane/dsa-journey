# [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/description/)

## Problem Statement
You are given a string `s`. You need to return the index of the first non-repeating character in it.
If there is no such character, return `-1`
**Example**
```python
Input: s = "leetcode"
Output: 0  # 'l' is the first non-repeating character
```
```python
Input: s = "loveleetcode"
Output: 2  # 'v' is the first unique character
```
```python
Input: s = "aabb"
Output: -1  # All characters repeat
```
## Possible Solutions – Brute Force to Optimized
## 1) One-Liner (Not recommended for interviews but cool for contests)
```python
return min([s.index(ch) for ch in set(s) if s.count(ch) == 1], default=-1)
```
> Not efficient because `count()` inside list comprehension is `O(n)`, so total `O(n²)` worst-case.

## 2) Check Frequency of Every Character (O(n²) time, O(1) space)
**Idea:** For each character in string `s`, count how many times it appears using a loop. If frequency is 1, return its index.

```python
for i in range(len(s)):
  cnt = 0
  for j in range(len(s)):
    if s[i] == s[j]: cnt += 1
  if cnt == 1: return i
return -1
```

## 3) Using HashMap to Store Frequencies (O(n) time, O(1) space)
**Idea:** 
1. Use a dictionary to store how many times each character appears.
2. Then loop again through string and return index of first character with frequency 1

```python
freq = {}
for ch in s:
  freq[ch] = freq.get(ch, 0) + 1

for i, ch in enumerate(s):
  if freq[ch] == 1: return i
return -1
```
OR Using `collections.Counter` (Pythonic & Fast)
```python
from collections import Counter

def firstUniqChar(s):
  freq = Counter(s)
  for i, ch in enumerate(s):
    if freq[ch] == 1: return i
return -1
```
> Same logic, just more elegant using built-in `Counter`.

## 4) Using an Array for Frequency (Optimized Constant Space)(Time: O(n), Space: O(1) → Just 26 integers)
**Why this works:** Only lowercase letters (a-z) → fixed-size array of 26.
> Uses ASCII values to map a → 0, b → 1, etc.

```python
freq = [0] * 26  # 26 lowercase letters

for ch in s:
  freq[ord(ch) - ord('a')] += 1
for i, ch in enumerate(s):
  if freq[ord(ch) - ord('a')] == 1: return i
return -1
```
> Most efficient for interviews