# [1974. Minimum Time to Type Word Using Special Typewriter](https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/)

## Problem Statement
You're using a special typewriter with only lowercase English letters arranged in a circle from 'a' to 'z'.

- The pointer initially points at letter 'a'.
- You can **type the character you're pointing at in 1 second**.
- You can **move the pointer clockwise or counterclockwise to the next letter**, which also takes 1 second per step.

Your task is: **Given a string `word`, return the minimum number of seconds to type it.**

---

## Examples
```python
Input: word = "abc"
Output: 5
# Explanation:
# From 'a' to 'a' → 0 moves + 1s to type
# 'a' to 'b' → 1 move + 1s to type
# 'b' to 'c' → 1 move + 1s to type → Total = 5s
```

```python
Input: word = "cba"
Output: 7
# Explanation:
# 'a' to 'c' = 2 moves (clockwise) + 1s to type
# 'c' to 'b' = 1 move + 1s to type
# 'b' to 'a' = 1 move + 1s to type → Total = 7s
```

```python
Input: word = "zaza"
Output: 8
# 'a' to 'z' = 1 move (counterclockwise) + 1s to type
# 'z' to 'a' = 1 move (clockwise) + 1s to type
# 'a' to 'z' = 1 move + 1s to type
# 'z' to 'a' = 1 move + 1s to type → Total = 8s
```

---

## Possible Solutions – Brute Force to Optimized

### 1) Brute Force Approach – Try All Directions

**Idea:**
- For each character, calculate both clockwise and counterclockwise distance manually
- Use `min` of both to decide shortest rotation time
- Add 1 second for typing each character

**Code:**
```python
def minTimeToType(word):
    pointer = 'a'
    time = 0
    for ch in word:
        dist = abs(ord(ch) - ord(pointer))
        time += min(dist, 26 - dist) + 1
        pointer = ch
    return time
```

**Time Complexity:** O(n) – one pass through the string  
**Space Complexity:** O(1)

---

### 2) Optimized Using ASCII and Modular Math (Concise)

**Idea:**
- Directly work with ASCII differences and circular nature of alphabet using `min` and `26 - diff`

**Code:**
```python
def minTimeToType(word):
    word = 'a' + word
    return sum(min(abs(ord(word[i]) - ord(word[i-1])), 26 - abs(ord(word[i]) - ord(word[i-1]))) for i in range(1, len(word))) + len(word)-1
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

### 3) Most Readable Interview Version

**Idea:**
- Start from 'a', loop each character
- Use `min(abs(curr - prev), 26 - abs(curr - prev))`
- Add 1 for each typing operation

**Code:**
```python
def minTimeToType(word):
    total_time = 0
    prev = 'a'
    for ch in word:
        diff = abs(ord(ch) - ord(prev))
        total_time += min(diff, 26 - diff) + 1
        prev = ch
    return total_time
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## Summary Table
| Approach                        | Time Complexity | Space Complexity | Interview Fit? |
|--------------------------------|------------------|-------------------|----------------|
| Brute Force Manual             | O(n)             | O(1)              | ✅              |
| Optimized ASCII Math           | O(n)             | O(1)              | ✅✅             |
| Most Readable Interview Style | O(n)             | O(1)              | ✅✅✅           |