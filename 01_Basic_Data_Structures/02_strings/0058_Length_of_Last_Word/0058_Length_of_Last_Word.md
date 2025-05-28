# [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/description/?envType=problem-list-v2&envId=string)

## Problem Statement
You're given a string s consisting of words and spaces. A word is defined as a maximal substring consisting of non-space characters only.  

**Task:** Return the length of the last word in the string.  
If the last word does not exist (e.g., empty string or only spaces), return 0.

---

## Examples

```python
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World", which has length 5.
```

```python
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: Last word is "moon"
```

```python
Input: s = "luffy is still joyboy"
Output: 6
Explanation: Last word is "joyboy"
```

---

## Possible Solutions – Brute Force to Optimized

### Brute Force – Split All Words and Return Last One
**Idea:**
- Use Python's split() which splits string by whitespace
- Get the last word using [-1]
- Return its length

```python
return len(s.split()[-1])
```
```python
words = s.split()
return len(words[-1]) if words else 0
```
OR if there are any trailing spaces
```python
return len(s.rstrip().split()[-1])
```
Time Complexity: O(n) — entire string split  
Space Complexity: O(n) — list of words stored  

✅ Easy and beginner-friendly  
⚠️ Avoid in memory-constrained environments  

---

### 2) Reverse Traverse – Count Last Word from Back (No Extra Space)
**Idea:**
- Start from end of string
- Skip trailing spaces
- Count characters till space or start

```python
def lengthOfLastWord(s: str) -> int:
    i = len(s) - 1
    length = 0

    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length
```
Time Complexity: O(n)  
Space Complexity: O(1)  

✅ ✅ Best for interviews — No extra space  
✅ Efficient and fast  

---

### 3) Regex Based Approach (for curiosity)
```python
import re
def lengthOfLastWord(s: str) -> int:
    matches = re.findall(r'\S+', s)
    return len(matches[-1]) if matches else 0
```
Time: O(n)  
Space: O(n)  

⚠️ Overkill for this problem  
❌ Avoid unless regex is specifically allowed  

---

### Hints & Key Observations
- String might have trailing spaces; must skip those
- Last word doesn’t always come after a space
- Don’t overuse .split() if space is a concern
- You only need to process from right side (optimized)

---

## Summary Table

| Approach                   | Time | Space | Interview Friendly? |
| -------------------------- | ---- | ----- | ------------------- |
| Brute Force (Split Words)  | O(n) | O(n)  | ✅                   |
| Reverse Traverse (Optimal) | O(n) | O(1)  | ✅✅✅                 |
| One-liner (rstrip + split) | O(n) | O(n)  | ❌ (space)           |
| Regex Approach             | O(n) | O(n)  | ❌ (overkill)        |
