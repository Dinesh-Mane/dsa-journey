# [2053. Kth Distinct String in an Array](https://leetcode.com/problems/kth-distinct-string-in-an-array/description/?envType=problem-list-v2&envId=hash-table)

## Problem Statement
A **distinct string** is a string that appears **only once** in an array.  
Given an array of strings `arr`, and an integer `k`, return the **k-th distinct string** present in `arr` (in the original order).  
If there are fewer than `k` distinct strings, return an empty string `""`.

---

## Examples
```
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"

Input: arr = ["a","b","a"], k = 3
Output: ""
```

---

## Solution 1: Brute Force (Two Loops)

### Idea:
For each string, check how many times it appears using `count()`. If it appears exactly once, it's distinct.

```python
def kthDistinct(arr, k):
    distinct = []
    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            distinct.append(arr[i])
    return distinct[k-1] if k <= len(distinct) else ""
```

- Time: O(n²)
- Space: O(n)
- Too slow for large input

---

## Solution 2: Use a HashMap to Count Frequency

### Idea:
Use `Counter` to get frequency in one pass. Then iterate in order and pick distinct ones.

```python
from collections import Counter

def kthDistinct(arr, k):
    freq = Counter(arr)
    for word in arr:
        if freq[word] == 1:
            k -= 1
            if k == 0:
                return word
    return ""
```

- Time: O(n)
- Space: O(n)
- ✅ Efficient and clean

---

## Solution 3: OrderedDict for Early Filtering

### Idea:
Same as above, but collect all distinct items in an OrderedDict to access directly by index.

```python
from collections import Counter, OrderedDict

def kthDistinct(arr, k):
    freq = Counter(arr)
    ordered = OrderedDict()
    for word in arr:
        if freq[word] == 1:
            ordered[word] = True
    if k > len(ordered):
        return ""
    return list(ordered.keys())[k-1]
```

- Time: O(n)
- Space: O(n)
- ✅ Maintains order while filtering early

---

## Solution 4: List Comprehension with Counter

### Idea:
Use a list comprehension to gather all strings with frequency 1 in original order.

```python
from collections import Counter

def kthDistinct(arr, k):
    freq = Counter(arr)
    distinct = [word for word in arr if freq[word] == 1]
    return distinct[k-1] if k <= len(distinct) else ""
```

- Time: O(n)
- Space: O(n)
- ✅ Very Pythonic

---

## Solution 5: Functional Approach with filter()

### Idea:
Same as list comprehension but using `filter()` for a functional programming approach.

```python
from collections import Counter

def kthDistinct(arr, k):
    freq = Counter(arr)
    distinct = list(filter(lambda x: freq[x] == 1, arr))
    return distinct[k-1] if k <= len(distinct) else ""
```

- Time: O(n)
- Space: O(n)
- Very clean if you're familiar with `filter`

---

## Optimal Solution (Recommended for Interviews)
**Solution 2 (HashMap + Loop)** is the best for interviews:
- ✅ Simple to code
- ✅ O(n) time
- ✅ Preserves order

Solution 4 (list comprehension) is also elegant.

---

## Hints for Similar Questions
1. Use `Counter()` to efficiently count items.
2. Be mindful of input **order** if the problem demands it.
3. Always check **k is within bounds**.
4. In interview, favor readable & optimal code.
5. Avoid `arr.count(x)` in loops – it's O(n)!