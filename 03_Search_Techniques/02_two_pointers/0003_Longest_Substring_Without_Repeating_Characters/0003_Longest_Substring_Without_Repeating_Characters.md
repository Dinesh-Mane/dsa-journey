# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=hash-table)

## Problem Statement
Given a string `s`, find the **length** of the **longest substring** without **repeating characters**.

---

## ✅ Examples

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc"

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b"

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke"
```

---

## Solution 1: Brute Force (All Substrings)
**Idea:**
Check all substrings. For each one, use a set to check for duplicates.

```python
def lengthOfLongestSubstring(s):
    max_len = 0
    n = len(s)
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len
```
- Time: O(n^2)
- Space: O(n)
- ❌ Too slow for large inputs

---

## Solution 2: Sliding Window (with Set)
**Idea:**
Use two pointers `left` and `right` to expand/shrink window. Use set to track unique chars.

```python
def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```
- Time: O(n)
- Space: O(n)
- ✅ Clean and efficient

---

## Solution 3: Sliding Window (with HashMap for Index)
**Idea:**
Instead of removing one-by-one, jump left pointer to right of last seen index.

```python
def lengthOfLongestSubstring(s):
    last_index = {}
    max_len = 0
    left = 0

    for right in range(len(s)):
        if s[right] in last_index and last_index[s[right]] >= left:
            left = last_index[s[right]] + 1
        last_index[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```
- Time: O(n)
- Space: O(n)
- ✅ Optimal for interviews

---

## Solution 4: Optimized with Array (Only for ASCII)
**Idea:**
Use array of size 128 instead of dict for better perf with ASCII chars.

```python
def lengthOfLongestSubstring(s):
    index = [-1] * 128
    left = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        if index[ord(char)] >= left:
            left = index[ord(char)] + 1
        index[ord(char)] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```
- Time: O(n)
- Space: O(1) → fixed size array
- ✅ Fastest when limited charset

---

## Solution 5: Pythonic with Enumerate + Slicing
**Idea:**
Simple logic with slicing and index lookup.

```python
def lengthOfLongestSubstring(s):
    longest = 0
    substring = ''
    for char in s:
        if char in substring:
            i = substring.index(char)
            substring = substring[i+1:]
        substring += char
        longest = max(longest, len(substring))
    return longest
```
- Time: O(n^2) in worst case
- Space: O(n)
- ❌ Not optimal, but readable

---

## Optimal Solution (Best for Interviews)
**Solution 3 (Sliding Window + HashMap)** is best:
- ✅ O(n) time
- ✅ Works with all characters
- ✅ Clear and understandable

---

## Hints for Similar Questions
1. Use sliding window to manage substrings efficiently
2. Use hashmap or set to check uniqueness quickly
3. Update window intelligently: avoid rechecking previous work
4. Optimize using ASCII tricks only if charset is known/fixed