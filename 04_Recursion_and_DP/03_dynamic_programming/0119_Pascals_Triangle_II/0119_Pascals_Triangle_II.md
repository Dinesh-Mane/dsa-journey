# [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/description/)
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.  
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:  

![](./PascalTriangle.gif)

## Examples:
```
Input: rowIndex = 3
Output: [1,3,3,1]

Input: rowIndex = 0
Output: [1]

Input: rowIndex = 1
Output: [1,1]
```

---

# 1. Brute-force Full Triangle, Return Last Row
## Step-by-step approach:

1. **Start with the first row `[1]`**
   * Initialize the result as `res = [[1]]`, which gives the 0th row of Pascal's Triangle.

2. **Iteratively build rows up to index `k`**
   * For each step from 1 to `k`:
     * Get the last row using `prev = res[-1]`.
     * Construct the new row as:
       * `1` at the beginning,
       * followed by `prev[i] + prev[i+1]` for all inner elements,
       * then `1` at the end.
     * This gives you the next Pascal's Triangle row based on the previous row.
     * Append it to `res`.

3. **Return the `k`th row**
   * After building up to the `k`th row, return `res[-1]`, which is the final result.

```python
def pt(k):
    res = [[1]]
    for _ in range(k):
        prev = res[-1]
        row = [1] + [prev[i]+prev[i+1] for i in range(len(prev)-1)] + [1]
        res.append(row)
    return res[-1]
```
OR
```python
res = []
n = k+1      # for 0-based index
for i in range(n):
    row = [1]*(i+1)
    for j in range(1,i):
        row[j] = res[i-1][j-1] + res[i-1][j]
    res.append(row)
return res[-1]
```

**Time:** O(k²)   
**Space:** O(k²)  

---

# 2. Row-by-Row, Single Array
## Step-by-step approach:
1. **Start with the first row `[1]`**
   * Initialize `row = [1]`, which represents the 0th row of Pascal’s Triangle.

2. **Iteratively update the row `k` times**
   * For each of the `k` iterations:
     * Generate a new row as:
       * `1` at the beginning,
       * followed by `row[i] + row[i+1]` for each pair of adjacent elements,
       * `1` at the end.
     * This gives you the next Pascal's Triangle row directly without storing all previous rows.
     * Update `row` with this new row.

3. **Return the final row**
   * After `k` updates, `row` will contain the `k`th row of Pascal’s Triangle, so return `row`.

```python
def pt(k):
    row = [1]
    for _ in range(k):
        row = [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]
    return row
```

**Time:** O(k²)  
**Space:** O(k)  

---

# 3. In-place from End to Start
## Step-by-step approach:
1. **Initialize a list with leading 1 and zeros**
   * Start with `row = [1] + [0]*k`
     → This gives you a list of size `k+1` with the first value as `1` and the rest as `0`.
     → It represents the 0th row and a placeholder for building up to the `k`th row.

2. **Iteratively build up the row**
   * Loop over each row index `i` from `1` to `k`:
     * For each `i`, update values from right to left (i.e., from `j = i` down to `1`):
       * Do `row[j] += row[j-1]` to simulate the Pascal’s Triangle addition rule.
       * This updates the current position based on the two elements above it.

3. **Return the final row**
   * After all iterations, `row` will contain the `k`th row of Pascal’s Triangle, so return `row`.

```python
def pt(k):
    row = [1] + [0]*k
    for i in range(1, k+1):
        for j in range(i, 0, -1):
            row[j] += row[j-1]
    return row
```

**Time:** O(k²)  
**Space:** O(k)  

---

# 4. Math (Binomial Coefficient)
## Step-by-step approach:
1. **Use `math.comb(k, i)` to compute each value in the k-th row**
   * For each index `i` from `0` to `k`, calculate the binomial coefficient `C(k, i)` using the built-in `comb` function.
     → This gives you the value at position `i` in the `k`th row of Pascal’s Triangle.

2. **Collect all values into a list**
   * Use a list comprehension to generate all such values from `i = 0` to `k`.
     → This gives you the entire `k`th row of Pascal’s Triangle in a single list.

```python
from math import comb
def pt(k):
    return [comb(k, i) for i in range(k+1)]
```

**Time:** O(k)  
**Space:** O(k)  

---

# 5. Using `reduce` + lambda
## Step-by-step approach:
1. **Start with the base row `[1]`**
   * This represents the 0-th row of Pascal’s Triangle.
     → This gives you the initial row to build upon.

2. **Iteratively apply the lambda function `k` times using `reduce`**
   * For each iteration, construct the next row by:
     * Adding `1` at both ends.
     * Replacing middle values with `r[i] + r[i+1]` from the previous row.
       → This builds the Pascal Triangle row-by-row up to the `k`th row.

3. **Return the final result after `k` iterations**
   * The final result from `reduce` is the `k`th row of Pascal’s Triangle.
     → `return final_row`

```python
from functools import reduce
def pt(k):
    return reduce(lambda r, _: [1]+[r[i]+r[i+1] for i in range(len(r)-1)]+[1], range(k), [1])
```

**Time:** O(k²)  
**Space:** O(k)  

---

# 6. Recursive with Memoization
## Step-by-step approach:
1. **Check the base case `k == 0`**
   * If true, return `[1]` directly.
     → This gives you the 0th row of Pascal’s Triangle.

2. **Recursively compute the previous row `pt(k-1)`**
   * Use `lru_cache` to memoize and avoid recomputation.
     → This gives you the full previous row efficiently.

3. **Build the current row using the previous row**
   * Add `1` at the start and end.
   * For each middle index `i`, compute `prev[i] + prev[i+1]`.
     → This constructs the `k`th row of Pascal’s Triangle.
4. **Return the final row**
   → `return current_row`

```python
from functools import lru_cache
@lru_cache(None)
def pt(k):
    if k == 0: return [1]
    prev = pt(k-1)
    return [1] + [prev[i]+prev[i+1] for i in range(len(prev)-1)] + [1]
```

**Time:** O(k²)  
**Space:** O(k²)  

---

# 7. NumPy Padding
## Step-by-step approach:
1. **Start with the first row `[1]` as a NumPy array**
   → This initializes the 0th row of Pascal’s Triangle.

2. **Repeat the following for `k` iterations**
   * Pad the current row with a zero on both ends using `np.pad(cur, (1,1), 'constant')`.
   * Create the next row by summing adjacent elements:
     * Left-shifted version: `[:-1]`
     * Right-shifted version: `[1:]`
       → This generates the next row based on the current row.

3. **Convert the final NumPy array to a list**
   → `return cur.tolist()` gives the `k`th row in standard Python list format.

```python
import numpy as np
def pt(k):
    cur = np.array([1])
    for _ in range(k):
        cur = np.pad(cur, (1,1), 'constant')[:-1] + np.pad(cur, (1,1), 'constant')[1:]
    return cur.tolist()
```

**Time:** O(k²)  
**Space:** O(k)  

---

# 8. Generator
## Step-by-step approach:
1. **Define an infinite generator `gen()` that yields Pascal rows one by one**
   * Start with `row = [1]`
   * In each iteration, yield the current row
   * Then update the row using Pascal’s Triangle logic:
     → `row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]`
     → This gives the next row by summing adjacent elements.

2. **Initialize the generator and advance it `k` times**
   * `g = gen()`
   * Use `next(g)` inside a loop to skip the first `k` rows.

3. **Return the next yielded value from the generator**
   * `return next(g)` gives the `(k)`th row directly.

```python
def pt(k):
    def gen():
        row = [1]
        while True:
            yield row
            row = [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]
    g = gen()
    for _ in range(k): next(g)
    return next(g)
```

**Time:** O(k²)  
**Space:** O(k)  

---

> Best for optimal + short: Solution 4 (Math + `comb()`)
> Best for manual logic + in-place DP: Solution 3