# [2000) Reverse Prefix of Word](https://leetcode.com/problems/reverse-prefix-of-word/description/?envType=problem-list-v2&envId=string)

Given a 0-indexed string `word` and a character `ch`, reverse the segment of `word` that starts at index `0` and ends at the index of the first occurrence of `ch` (inclusive). If the character ch does not exist in word, do nothing.
> For example, if `word = "abcdefd"` and `ch = "d"`, then you should reverse the segment that starts at `0` and ends at `3` (inclusive). The resulting string will be `"dcbaefd"`.

Return the resulting string.

### Examples
```
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"

Input: word = "abcd", ch = "z"
Output: "abcd"
```

# Solution 1: Brute-force using loop and slicing
Time: O(n) | Space: O(n)

```python
def reversePrefix(word: str, ch: str) -> str:
    for i in range(len(word)):
        if word[i] == ch:
            return word[:i+1][::-1] + word[i+1:]
    return word
```
# Solution 2: Using str.find() and slicing
Time: O(n) | Space: O(n)

```python
def reversePrefix(word: str, ch: str) -> str:
    idx = word.find(ch)
    return word[:idx+1][::-1] + word[idx+1:] if idx != -1 else word
```
# Solution 3: Using list conversion and manual reversal
Time: O(n) | Space: O(n)
```python
def reversePrefix(word: str, ch: str) -> str:
    idx = word.find(ch)
    if idx == -1:
        return word
    word_list = list(word)
    l, r = 0, idx
    while l < r:
        word_list[l], word_list[r] = word_list[r], word_list[l]
        l += 1
        r -= 1
    return ''.join(word_list)
```
# Solution 4: In-place reversal (simulated)
Note: Python strings are immutable, so we simulate in-place by converting to a list.

Time: O(n) | Space: O(n)

```python
def reversePrefix(word: str, ch: str) -> str:
    idx = word.find(ch)
    if idx == -1:
        return word
    word = list(word)
    for i in range((idx + 1) // 2):
        word[i], word[idx - i] = word[idx - i], word[i]
    return ''.join(word)
```
# Solution 5: Using itertools (just for variety)
Time: O(n) | Space: O(n)
```python
from itertools import islice

def reversePrefix(word: str, ch: str) -> str:
    idx = word.find(ch)
    if idx == -1:
        return word
    prefix = ''.join(reversed(list(islice(word, idx + 1))))
    return prefix + word[idx + 1:]
```