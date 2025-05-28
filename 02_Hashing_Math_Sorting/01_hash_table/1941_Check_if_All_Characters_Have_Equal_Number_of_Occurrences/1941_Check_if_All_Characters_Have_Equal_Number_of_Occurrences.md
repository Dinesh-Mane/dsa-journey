# [1941. Check if All Characters Have Equal Number of Occurrences](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/?envType=problem-list-v2&envId=hash-table)
Given a string `s` of lowercase letters, determine whether all characters that appear in the string appear the same number of times.

# Solution 1: Brute-force using count() for every char
```python
def areOccurrencesEqual(s):
    for c in set(s):
        if s.count(c) != s.count(s[0]): return False
    return True
```
Time Complexity: O(n^2)
Space Complexity: O(1)

# Solution 2: Hashmap with manual check
```python
def areOccurrencesEqual(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    values = list(freq.values())
    return all(val == values[0] for val in values)
```
Time Complexity: O(n)
Space Complexity: O(1) (max 26 lowercase letters)

# Solution 3: Use collections.Counter and check all values
```python
from collections import Counter
def areOccurrencesEqual(s):
    return len(set(Counter(s).values())) == 1
```
Time Complexity: O(n)
Space Complexity: O(1)

# Solution 4: Use frequency array (since only lowercase letters)
```python
def areOccurrencesEqual(s):
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    count = 0
    for n in freq:
        if n:
            if count == 0: count = n
            elif n != count: return False
    return True
```
Time Complexity: O(n)
Space Complexity: O(1)

# Solution 5: Functional style with Counter
```python
from collections import Counter
def areOccurrencesEqual(s):
    return len({*Counter(s).values()}) == 1
```
Time Complexity: O(n)
Space Complexity: O(1)

---

# Summary table

| Solution | Approach                               | Time  | Space |
| -------- | -------------------------------------- | ----- | ----- |
| 1        | Brute-force with `count()`             | O(n²) | O(1)  |
| 2        | Manual frequency dict check            | O(n)  | O(1)  |
| 3        | `collections.Counter` with set check   | O(n)  | O(1)  |
| 4        | Array-based freq count                 | O(n)  | O(1)  |
| 5        | One-liner with unpacked Counter values | O(n)  | O(1)  |