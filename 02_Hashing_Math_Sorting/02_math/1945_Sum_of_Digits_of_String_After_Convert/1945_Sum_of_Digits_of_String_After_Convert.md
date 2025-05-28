# [1945. Sum of Digits of String After Convert](https://leetcode.com/problems/sum-of-digits-of-string-after-convert/)

## Problem Statement
You are given a string `s` consisting of lowercase English letters, and an integer `k`.

- First, **convert** `s` to a string of digits by replacing each letter with its position in the alphabet (i.e. 'a' -> 1, 'b' -> 2, ..., 'z' -> 26).
- Then, **transform** the string `k` times by:
    - Taking the sum of the digits,
    - Converting the sum into a string,
    - Repeating this process `k` times.

Return the resulting integer after performing the operations.

**Example**
```python
Input: s = "zbax", k = 2
Output: 8
# Explanation:
# "z" -> 26, "b" -> 2, "a" -> 1, "x" -> 24 → converted to "262124"
# Sum of digits: 2+6+2+1+2+4 = 17
# Second transform: 1+7 = 8 → final result
```
```python
Input: s = "leetcode", k = 2
Output: 6
```
```python
Input: s = "zbax", k = 2
Output: 8
```

---

## Possible Solutions – Brute Force to Optimized

### 1) Brute Force Approach (Manual conversion and repeated string handling)

**Idea:**
- Convert characters to numbers by looking up position.
- Join digits into string and repeat `k` transformations of digit sum.

**Code:**
```python
def getLucky(s, k):
    num = ''.join(str(ord(c) - ord('a') + 1) for c in s)
    for _ in range(k):
        num = str(sum(int(ch) for ch in num))
    return int(num)
```

**Time Complexity:**
- Conversion: O(n) where `n` is length of string `s`
- Each transformation: O(m), where `m` is number of digits (bounded)
- Total: **O(n + k·m)** ≈ O(n) for practical constraints

**Space Complexity:** O(n) to store the numeric string

---

### 2) Slightly Optimized – Reduce to Integer Earlier

**Idea:**
- Immediately sum characters' positional values and work on digits only

**Code:**
```python
def getLucky(s, k):
    total = sum(int(d) for c in s for d in str(ord(c) - ord('a') + 1))
    for _ in range(k - 1):
        total = sum(int(d) for d in str(total))
    return total
```

**Time Complexity:** O(n + k·m)
- Slightly less overhead than brute since no need to store long intermediate string

**Space Complexity:** O(1)
- Only a few integer vars used

---

### 3) Optimized Version – Using Digit Sum Helper

**Idea:**
- Add a helper function to cleanly handle digit sum logic

**Code:**
```python
def getLucky(s, k):
    def digit_sum(n):
        return sum(int(d) for d in str(n))

    total = sum(int(d) for c in s for d in str(ord(c) - ord('a') + 1))
    for _ in range(k - 1):
        total = digit_sum(total)
    return total
```

**Time Complexity:** O(n + k·m)
**Space Complexity:** O(1)

---

### 4) Most Concise & Optimal for Interviews (1-liner body)

**Code:**
```python
def getLucky(s, k):
    total = sum(int(d) for c in s for d in str(ord(c) - 96))
    for _ in range(k - 1):
        total = sum(int(d) for d in str(total))
    return total
```

✅ This is the **best version to use in interviews**:
- Concise ✅
- Efficient ✅
- Clean logic ✅

**Time Complexity:** O(n + k·m)
**Space Complexity:** O(1)

---

## Summary Table
| Approach                          | Time Complexity | Space Complexity | Interview Fit? |
|----------------------------------|------------------|-------------------|----------------|
| Brute Force                      | O(n + k·m)       | O(n)              | ❌              |
| Slight Optimization              | O(n + k·m)       | O(1)              | ✅              |
| Optimized with Helper            | O(n + k·m)       | O(1)              | ✅              |
| Most Concise & Optimal           | O(n + k·m)       | O(1)              | ✅✅✅           |