# [2131. Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/)

## Problem Statement
You are given an array of strings `words` where each word contains exactly two lowercase English letters.

**Task**: Return the length of the longest palindrome that can be built by concatenating words from the array.  
Each word can be used **at most once**.
### Core Idea:
- Palindromes read the same backward and forward.
- If you find a word and its reverse, you can use both (e.g., "ab" + "ba").
- Words like "aa", "bb" (same letters) can be:
  - Used in pairs, OR
  - Placed at the center (only 1 allowed for center)

---

## Examples

```python
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One palindrome is "lcggcl", which has length 6.
```

```python
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One palindrome is "abtyytba" or "lcyyttcl".
```

```python
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
```

---

## Possible Solutions – Brute Force to Optimized

### 1) Brute Force (Try all word combinations → Check palindrome)
**Idea:** 
- Generate all permutations of words.
- Concatenate each, check if it's a palindrome.
- Track max length.

```python
# ❌ Not recommended - Too slow
from itertools import permutations

def longestPalindrome(words):
    max_len = 0
    for k in range(1, len(words)+1):
        for perm in permutations(words, k):
            s = ''.join(perm)
            if s == s[::-1]:
                max_len = max(max_len, len(s))
    return max_len
```
 
Time: O(n!) | Space: O(n)    
⚠️ Too slow for large inputs  
⚠️ Not suitable for interviews  

---

### 2) HashMap Counting Approach
**Idea:**
- Count frequency of each word.
- For each word, check if its reverse exists in map.
- If yes, pair them up: 1 from word, 1 from reverse.
- Special care: for words like "aa", "bb" – we can use one in center.

```python
from collections import Counter

def longestPalindrome(words):
    count = Counter(words)
    res = 0
    used_center = False

    for word in list(count.keys()):
        rev = word[::-1]
        if word != rev:
            pairs = min(count[word], count[rev])
            res += pairs * 4
            count[word] -= pairs
            count[rev] -= pairs
        else:
            pairs = count[word] // 2
            res += pairs * 4
            count[word] -= pairs * 2

    # Check if any "center word" like "aa" is still left
    for word in count:
        if word[0] == word[1] and count[word] > 0:
            res += 2
            break

    return res
```
Time: O(n) | Space: O(n)  
✅ Perfect for interviews  
✅ Clean, efficient, logical  

---

### 3) Optimized 2D Array (fixed 26x26 count table)
**Idea:**  
- Only 26x26 = 676 possible 2-letter lowercase combos.
- Map each word to `count[char1][char2]`
- If reverse already exists in matrix, pair it immediately.

```python
def longestPalindrome(words):
    count = [[0]*26 for _ in range(26)]
    res = 0
    for word in words:
        a, b = ord(word[0]) - ord('a'), ord(word[1]) - ord('a')
        if count[b][a]:
            res += 4
            count[b][a] -= 1
        else:
            count[a][b] += 1
    for i in range(26):
        if count[i][i] > 0:
            res += 2
            break
    return res
```
Time: O(n) | Space: O(1) – fixed 26x26 table  
✅ Ultra fast  
✅ Best for large inputs  
✅ Still readable & interview-acceptable  

---

### 4) Slight Variation: Greedy Using Set
**Idea:**
- Track used words using set
- Try to form mirror pairs like “ab” + “ba”
- Use palindromic word like “cc” in the middle

```python
def longestPalindrome(words):
    seen = set()
    center_used = False
    res = 0

    for word in words:
        rev = word[::-1]
        if rev in seen:
            res += 4
            seen.remove(rev)
        else:
            seen.add(word)

    for w in seen:
        if w[0] == w[1]:
            res += 2
            break

    return res
```
⚠️ Simpler but may fail edge cases where same word appears multiple times (e.g. "aa", "aa", "aa")  
Not perfect unless counts are considered  

---

### Hints
- For each word, try to pair it with its reverse (e.g., "ab" + "ba")
- If the word is the same as its reverse (e.g., "aa"), you can:
  - Use 2 in pairs
  - Keep 1 for the center (but only once!)
- Result = `4 * number_of_pairs + 2 (optional center)`

---

## Summary Table

| Approach                 | Time  | Space | Notes                       |
| ------------------------ | ----- | ----- | --------------------------- |
| Brute Force Permutations | O(n!) | O(n)  | ❌ Very inefficient          |
| HashMap Counting         | O(n)  | O(n)  | ✅ Clean and interview ready |
| 2D Array Count           | O(n)  | O(1)  | ✅✅ Fastest and optimal      |
| Greedy with Set (Flawed) | O(n)  | O(n)  | ⚠️ May miss duplicates      |