# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

## Problem Statement
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
> A string is a palindrome when it reads the same forward and backward.

**Constraints:**  
- You must ignore all non-alphanumeric characters (punctuation, spaces, etc.)
- Ignore case sensitivity (`'A' == 'a'`, `'Z' == 'z'`)
- Return `True` if it’s a palindrome, else `False`

**Example**
```python
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```
```python
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```
```python
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force – Clean the string, then reverse and compare (O(n) time, O(n) space)
**Idea:**  
1. Remove all non-alphanumeric characters manually.
2. Lowercase the cleaned string.
3. Compare it with its reverse.

```python
cleaned = ''
for c in s:
  if c.isalnum(): cleaned += c.lower()
return cleaned == cleaned[::-1]
```
to check palindrom string we can use both:
```python
cleaned == cleaned[::-1]

# OR

left = 0 
right = len(s) - 1

while left < right:
  if s[left] != s[right]: return False
  left += 1
  right -= 1
return True
```
## 2) Using List Comprehension + `join()` (O(n log n + m log m) Time, O(1) Space)
Improved version of brute-force
```python
cleaned = ''.join(c.lower() for c in s if c.isalnum())
return cleaned == cleaned[::-1]
```
you can use both 
```python
# Option 1: List comprehension
cleaned = ''.join([c.lower() for c in s if c.isalnum()])

# Option 2: Generator expression (no square brackets)
cleaned = ''.join(c.lower() for c in s if c.isalnum())
```

## 3) Regex + Slicing – Concise but not the fastest
Use regular expressions to remove non-alphanumeric characters

```python
import re

def isPalindrome(s: str) -> bool:
  cleaned = re.sub('[^a-zA-Z0-9]', '', s).lower()
  return cleaned == cleaned[::-1]
```
> `[^a-zA-Z0-9]` is a regular expression pattern that matches any single character except for those in the range `a-z`, `A-Z`, or `0-9`. In other words, it matches all characters except alphabets and numbers.  
> If a matching character is found, we will replace it with an empty string.  
> Tradeoff: concise but slower than two pointers due to regex processing.

## 4) Using Two Pointers (Optimal) – O(n) time, O(1) space
**Idea:** Instead of creating a new cleaned string, we can use two pointers (left and right), and scan from both ends.
- Skip non-alphanumeric characters on both sides.
- Compare lowercase values at each step.

```python
left, right = 0, len(s) - 1

while left < right:
  while left < right and not s[left].isalnum(): left += 1     # skip non-alphanumeric on left
  while left < right and not s[right].isalnum(): right -= 1   # skip non-alphanumeric on right
  if s[left].lower() != s[right].lower(): return False  # compare lowercased chars
  left += 1
  right -= 1
return True
```