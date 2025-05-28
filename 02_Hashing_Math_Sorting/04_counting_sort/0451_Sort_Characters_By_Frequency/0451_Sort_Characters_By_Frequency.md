# [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/description/)
## Problem Statement:
Given a string `s`, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

## Examples
```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

# Possible solutions:
# Sol 1: Counter + Sort
## ✅ Core Idea
1. **Count Frequencies:** We use Counter to count how many times each character appears in the string.
2. **Sort by Frequency (Descending):** Sort the characters based on their frequency using `sorted(c.items(), key=lambda x: -x[1])`.
3. **Build Output:** For each character-frequency pair in the sorted list, multiply the character by its frequency and join the result.

```python
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return ''.join(ch * freq for ch, freq in sorted(c.items(), key=lambda x: -x[1]))
```
Time: O(n log k) (k = unique chars)  
Space: O(k)  

# Sol 2: Counter + Bucket Sort
This approach leverages bucket sort for linear-time grouping based on frequencies.

## Step-by-Step Logic
1. **Count Frequencies:** Use `Counter(s)` to count how many times each character appears.
2. **Create Buckets:** Make a list `b` of size `len(s)+1`, where index `i` represents characters that appear exactly `i` times.
3. **Fill Buckets:** For each `(char, freq)` in the Counter, append `char` to `b[freq]`.
4. **Build Output String:** Iterate from high frequency to low (`range(len(b)-1, 0, -1)`) and repeat each character `i` times for that bucket.

```python
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        b = [[] for _ in range(len(s)+1)]
        for ch, freq in c.items():
            b[freq].append(ch)
        return ''.join(ch * i for i in range(len(b)-1, 0, -1) for ch in b[i])
```
Time: O(n)  
Space: O(n)  

---

### Recommended in Interviews:
- Sol 1: Counter + Sort - ✅ Very good for interviews — clean and easy to explain.
- Sol 2: Counter + Bucket Sort - Best for interviews if you want to impress with optimal logic.

---

# Sol 3: Heap
This approach uses a max heap to sort characters by frequency in descending order.

## Step-by-Step Logic
1. **Count Frequencies:** Use `Counter(s)` to get character frequencies.
2. **Build Max Heap:** Create a list of tuples `(-freq, char)` so the highest frequency becomes the smallest number (Python only has a min-heap).
Example: `('a': 3)` becomes `(-3, 'a')`.
3. **Heapify:** Use `heapq.heapify()` to build the heap in `O(k)` time, where `k` is the number of unique characters.
4. **Construct Output:** Pop from the heap and multiply each character `-freq` times to build the output string.

```python
import heapq
from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        h = [(-f, ch) for ch, f in c.items()]
        heapq.heapify(h)
        return ''.join(ch * -f for f, ch in h)
```
Time: O(n log k)  
Space: O(k)  

# Sol 4: Sorted + Lambda
This is a very concise one-liner solution using Python’s built-in `sorted()` function with a custom lambda function to sort characters by frequency.

## Step-by-Step Logic
1. Sort Characters:
    - For each character `x`:
        - `s.count(x)` gives the frequency of `x` in the string.
        - `-s.count(x)` ensures sorting in descending frequency.
        - `x` is used as a tie-breaker in lexicographical order.
2. Join Sorted Characters:
    - After sorting, use `''.join(...)` to get the final string.


```python
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(sorted(s, key=lambda x: (-s.count(x), x)))
```
Time: O(n²)  
Space: O(n)  

