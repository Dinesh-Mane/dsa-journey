# [1961. Check If String Is a Prefix of Array](https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/)

## Problem Statement
You are given a string `s` and an array of strings `words`.

**Task**: Return `True` **if** `s` is a prefix string of `words`. Otherwise, return `False`.

A string `s` is said to be a **prefix string** of `words` **if** `s` can be formed by **concatenating the first `k` strings** from `words`, where `k >= 1` and `k <= len(words)`.

---

## Examples

```python
Input: s = "iloveleetcode", words = ["i", "love", "leetcode", "apples"]
Output: True
# Explanation: "i" + "love" + "leetcode" = "iloveleetcode" ✅
```

```python
Input: s = "iloveleetcoding", words = ["i", "love", "leetcode", "apples"]
Output: False
# Explanation: "i" + "love" + "leetcode" = "iloveleetcode" ≠ "iloveleetcoding"
```

```python
Input: s = "a", words = ["a"]
Output: True
```

---

## Possible Solutions – Brute Force to Optimized

### 1) Brute Force – Concatenate One by One and Compare Each Time

**Idea:**
- Start from empty string
- Keep concatenating words from the list
- After each step, check if it equals `s`
- If ever equal, return `True`. If it becomes longer than `s`, return `False`

```python
def isPrefixString(s, words):
    curr = ""
    for word in words:
        curr += word
        if curr == s:
            return True
        if len(curr) > len(s):
            return False
    return False
```

**Time Complexity:** O(n), where `n` = len(s) (we build string once up to s length)  
**Space Complexity:** O(n) (temporary string built)

✅ Works fine for small inputs. Very intuitive for interviews.

---

### 2) Smarter String Slice Check – No Need to Build Fully

**Idea:**
- Maintain an index in `s`
- For each word in `words`, check if that word matches slice of `s`
- If mismatch at any point, return False
- If index reaches exactly end of `s`, return True

```python
def isPrefixString(s, words):
    i = 0
    for word in words:
        if s[i:i+len(word)] != word:
            return False
        i += len(word)
        if i == len(s):
            return True
    return False
```

**Time Complexity:** O(n), one full pass on `s` and `words`  
**Space Complexity:** O(1)  

✅ This is optimal for interviews.  
✅ No extra memory used for string building

---

### 3) Pythonic One-Liner (for understanding, not interviews)

```python
def isPrefixString(s, words):
    return s == ''.join(words)[:len(s)]
```

**Time Complexity:** O(n), joins full string and slices  
**Space Complexity:** O(n), creates one joined string  

⚠️ **Note**: Less efficient in large inputs, avoid in strict interviews

---

### 4) Greedy + Early Exit (Hybrid of above two)

```python
def isPrefixString(s, words):
    total = ""
    for word in words:
        total += word
        if total == s:
            return True
        if len(total) > len(s):
            return False
    return False
```

Time: O(n), Space: O(n)  
> Similar to Brute Force; included for completeness

---

### Hints
- You only need the prefix of `words` array, not all elements
- Once concatenated string length > `s`, you can safely return False early
- Use slicing to avoid unnecessary string building

---

## Summary Table

| Approach                          | Time Complexity | Space Complexity | Interview Fit? |
|----------------------------------|------------------|-------------------|----------------|
| Brute Force String Build         | O(n)             | O(n)              | ✅              |
| Index-wise Slice Check           | O(n)             | O(1)              | ✅✅✅           |
| Pythonic One-liner               | O(n)             | O(n)              | ❌ (Not ideal)  |
| Greedy + Early Return            | O(n)             | O(n)              | ✅              |
