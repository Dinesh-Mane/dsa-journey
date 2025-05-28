# [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/description/)

## Problem Statement
Given a string s, reverse the characters of each word in the string, keeping the word order and spaces unchanged.

**Constraints:**  
- Words are separated by single spaces.
- There are no leading or trailing spaces.
- Do it efficiently, preferably in-place if working with a character array.

**Example**
```python
Input:  s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```
```python
Input: s = "Mr Ding"
Output: "rM gniD"
```

## Possible Solutions – Brute Force to Optimized
## 1) Brute Force – Split, Reverse, Join - O(n) time, O(n) space (extra space for list)

**In-place? -> No**
```python
words = s.split(" ")                     # split by space
reversed_words = [word[::-1] for word in words]     # reverse each
return " ".join(reversed_words)             # join back
```
> Works well and easy to implement, but not in-place

## 2) Slight Optimization ( Time: O(n), Space: O(n) )
**Idea:** Same logic as above but compressed.  
**In-place? -> No**  
```python
return ' '.join([w[::-1] for w in s.split()])
```
OR
```python
return ' '.join(w[::-1] for w in s.split())
```
> Pythonic and clean, but still O(n) space.

## 3) Manual Word Processing (char by char) ( Time: O(n), Space: O(n) )

**Idea:** 
- Traverse string character-by-character
- Build each word, reverse it, then append it to result

**In-place? -> No**
```python
res = []
word = []
for ch in s:
  if ch == ' ':
    res.extend(word[::-1])
    res.append(' ')
    word = []
  else: word.append(ch)
res.extend(word[::-1])  # reverse last word
return ''.join(res)
```
> Better control, still O(n) space.

## 4) Stack-based Reversal (O(n) Time, O(n) Space)
**In-place? -> No**
```python
res = []
st = []
for c in s:
  if c == ' ':
    while st: res.append(st.pop())
    res.append(' ')
  else: st.append(c)
while st:
  res.append(st.pop())
return ''.join(res)
```

 
## 5) In-place Word Reverse (For Mutable List Input) ( Time: O(n), Space: O(1) )
**Used when input is a list of characters**, e.g., `s = list("Let's take LeetCode contest")`  
**Idea:**
- Traverse the char array.
- When you find a word, reverse it in-place using two-pointer.

**In-place? -> Yes**
```python
def reverse(l, r):
  while l < r:
    s[l], s[r] = s[r], s[l]
    l += 1
    r -= 1

start = 0
for end in range(len(s)):
  if s[end] == ' ':
    reverse(start, end - 1)
    start = end + 1
reverse(start, len(s) - 1)   # last word
```
> Fully in-place, very interview-friendly!

## Bonous: 6. Using Regex (Quick but Not Optimal for Interviews) (Time: O(n), Space: O(n))
**In-place? -> No**
```python
import re
def reverseWords(s):
  return ' '.join(re.findall(r'\S+', s)[::-1])
```
> May not be accepted in strict interview settings.

# Summary
| Approach                    | Time Complexity | Space Complexity | In-place? | Interview Worthy? |
| --------------------------- | --------------- | ---------------- | --------- | ----------------- |
| Brute-force split + reverse | O(n)            | O(n)             | ❌         | ✅ (easy/clean)    |
| Pythonic list comprehension | O(n)            | O(n)             | ❌         | ✅ (if allowed)    |
| Char-by-char processing     | O(n)            | O(n)             | ❌         | ✅✅ (good control) |
| Stack-based word reverse    | O(n)            | O(n)             | ❌         | ✅ (educational)   |
| In-place for char array     | O(n)            | O(1)             | ✅         | ✅✅✅ (Best)        |
| Regex-based split           | O(n)            | O(n)             | ❌         | ❌ (not preferred) |