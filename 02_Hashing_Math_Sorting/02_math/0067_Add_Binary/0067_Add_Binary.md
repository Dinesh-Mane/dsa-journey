# [67. Add Binary](https://leetcode.com/problems/add-binary/description/)

## Problem Statement
Given two binary strings a and b, return their sum as a binary string.

**Constraints:**  
- Each string contains only '0' or '1'
- Input strings will not be empty
- Strings can be long (up to 10⁴ chars)

---

## Examples

```python
Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"
```

---

## Possible Solutions – Brute Force to Optimized

### 1) Brute Force – Manual Conversion to Decimal → Add → Convert Back to Binary
**Idea:** Convert both binary strings to integers (base 2), add them, and convert back to binary.

**Steps:**
- Convert a to integer using `int(a, 2)`
- Convert b to integer using `int(b, 2)`
- Add both integers
- Convert the result to binary using `bin(result)`
- Remove the `0b` prefix from binary string

```python
return bin(int(a, 2) + int(b, 2))[2:]
```
Time Complexity: O(n + m)  
Space Complexity: O(1)  
⚠️ Not allowed in many interviews as it avoids simulating actual binary addition. Too dependent on Python's built-in power.

---

### 2) Manual Addition (Simulated Binary Addition – Like School Method)
**Idea:** Add binary digits from right to left, simulating the carry like we do in addition on paper.

**Steps:**  
1. Initialize pointers `i = len(a) - 1`, `j = len(b) - 1`
2. Initialize carry = 0
3. Use a result list to build the answer from the end
4. Loop while `i >= 0 or j >= 0 or carry`
   - Extract digit from `a` if `i >= 0`, else 0
   - Extract digit from `b` if `j >= 0`, else 0
   - Sum the digits with carry
   - Append `sum % 2` to result (binary digit)
   - Update carry = `sum // 2`
   - Decrement `i` and `j`
5. After loop ends, reverse the result list and join as string

```python
def addBinary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []

    while i >= 0 or j >= 0 or carry:
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0

        total = bit_a + bit_b + carry
        res.append(str(total % 2))
        carry = total // 2

        i -= 1
        j -= 1

    return ''.join(reversed(res))
```
Time Complexity: O(max(n, m))  
Space Complexity: O(max(n, m))  
✅ Most recommended approach for interviews – simulates actual binary addition.  

---

### 3) Manual Addition Using `collections.deque` (Avoids reversing at the end)
`Idea:` Use a deque instead of a list so we can appendleft instead of reversing later.

```python
from collections import deque

def addBinary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = deque()

    while i >= 0 or j >= 0 or carry:
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0

        total = bit_a + bit_b + carry
        res.appendleft(str(total % 2))
        carry = total // 2

        i -= 1
        j -= 1

    return ''.join(res)
```
Time Complexity: O(max(n, m))  
Space Complexity: O(max(n, m))  
✅ Slightly neater for large inputs to avoid reversal.  

---

### 4) Optimized with zip_longest (from itertools)
**Idea:** Use zip_longest to iterate over both strings in reverse simultaneously, filling missing digits with '0'

```python
from itertools import zip_longest

def addBinary(a: str, b: str) -> str:
    carry = 0
    result = []

    for x, y in zip_longest(reversed(a), reversed(b), fillvalue='0'):
        total = int(x) + int(y) + carry
        result.append(str(total % 2))
        carry = total // 2

    if carry:
        result.append('1')

    return ''.join(reversed(result))
```
Time Complexity: O(max(n, m))  
Space Complexity: O(max(n, m))  
✅ Pythonic and clean – good for interviews with Python-friendly companies  

---


## Summary Table

| Approach                             | Time         | Space        | Interview Friendly? | Comments                                   |
| ------------------------------------ | ------------ | ------------ | ------------------- | ------------------------------------------ |
| Brute-force with `int()` and `bin()` | O(n + m)     | O(1)         | ❌                   | Avoid in interviews – not simulating logic |
| Manual Addition (School method)      | O(max(n, m)) | O(max(n, m)) | ✅✅✅                 | Most preferred in interviews               |
| With `deque`                         | O(max(n, m)) | O(max(n, m)) | ✅✅                  | Efficient – avoids reversal                |
| With `zip_longest`                   | O(max(n, m)) | O(max(n, m)) | ✅✅                  | Pythonic and clean                         |