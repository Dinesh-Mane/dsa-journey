# [1967. Number of Strings That Appear as Substrings in Word](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/)

## Problem Statement
You're given an array of strings `patterns` and a string `word`.

**Task**: Return the number of strings in `patterns` that are **substrings** of `word`.

## Examples
```python
Input: patterns = ["a", "abc", "bc", "d"], word = "abc"
Output: 3
# Explanation: "a", "abc", "bc" are substrings of "abc" ✅
```

```python
Input: patterns = ["a", "b", "c"], word = "aaaaabbbbb"
Output: 2
```

---

## Possible Solutions – Brute Force to Optimized
### 1) Brute Force – Check Every Pattern Using `in`
**Idea:** For each pattern in patterns, check if it is in the word using Python's `in` keyword

```python
def numOfStrings(patterns, word):
    count = 0
    for p in patterns:
        if p in word:
            count += 1
    return count
```

**Time Complexity:** O(n * m), where n = len(patterns), m = average length of word  
**Space Complexity:** O(1)  

✅ Very intuitive for interviews
✅ Best if built-in substring search is allowed

---

### 2) Use List Comprehension (Pythonic One-Liner)

```python
def numOfStrings(patterns, word):
    return sum(p in word for p in patterns)
```

Time: O(n * m)  
Space: O(1)  

⚠️ Not recommended in interviews unless asked to golf code
✅ Good for short, elegant scripts

---

### 3) Manual Substring Matching (Naive Sliding Window)

**Idea:**
- For each pattern, slide over the `word` and manually compare
- Avoid `in` keyword if not allowed

```python
def numOfStrings(patterns, word):
    def is_substring(p, w):
        for i in range(len(w) - len(p) + 1):
            if w[i:i+len(p)] == p:
                return True
        return False

    count = 0
    for p in patterns:
        if is_substring(p, word):
            count += 1
    return count
```
OR
```python
def numOfStrings(self, patterns: List[str], word: str) -> int:
    cnt = 0
    for p in patterns:
        for i in range(len(word)-len(p)+1):
            if word[i:i+len(p)]==p:
                cnt+=1
                break
    return cnt
```


**Time Complexity:** O(n * m * k), where k is length of each pattern  
**Space Complexity:** O(1)  

✅ Good if interviewers ask you to write `in` manually

---

### 4) Knuth-Morris-Pratt (KMP) Algorithm – For Interview Challenge

**Idea:**
- For each pattern, use KMP algorithm to find whether it's in the word
- Avoids naive sliding window by using prefix table

```python
def kmp_search(pattern, text):
    lps = [0] * len(pattern)
    j = 0
    
    # Build lps array
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    # Pattern match
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return True
    return False

def numOfStrings(patterns, word):
    count = 0
    for p in patterns:
        if kmp_search(p, word):
            count += 1
    return count
```

Time: O(n * (m + k))  
Space: O(k) for each pattern's lps array  

✅ Use when asked for efficient substring search

---

## Summary Table
| Approach                           | Time Complexity      | Space Complexity | Interview Fit? |
|-----------------------------------|-----------------------|------------------|----------------|
| Brute Force `in` check            | O(n * m)              | O(1)             | ✅✅✅           |
| List Comprehension                | O(n * m)              | O(1)             | ✅              |
| Manual Sliding Window             | O(n * m * k)          | O(1)             | ✅              |
| KMP Algorithm                     | O(n * (m + k))        | O(k)             | ✅✅ (advanced)  |

---

### Hints
- Python's `in` is already optimized for substring search
- Avoid extra string concatenation
- If asked, be ready to explain or implement your own matcher like KMP