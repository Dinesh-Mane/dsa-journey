# [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)
Given an integer numRows, return the first numRows of Pascal's triangle.  
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![](./PascalTriangle.gif)

## Examples:
```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]
```

---

# 1. Basic Iterative Approach
## Step-by-Step approach:
1. **Initialize the triangle**
   * Start with `res = [[1]]` to represent the first row.

2. **Iterate for remaining rows**
   * For each row from 1 to `n-1`:
     * Get the previous row using `prev = res[-1]`.
     * Compute the middle values using a list comprehension: `[prev[i] + prev[i+1] for i in range(len(prev)-1)]`.
     * Form the new row as `[1] + ... + [1]` using the computed values.
     * Append the new row to the result using `res.append(row)`.

3. **Return the triangle**
   * After completing the loop, return the full triangle with `return res`.

> This is a bottom-up approach where each row is built based on the previous one by adding adjacent values.

```python
def pt(n):
    res = [[1]]
    for _ in range(1, n):
        prev = res[-1]
        row = [1] + [prev[i] + prev[i+1] for i in range(len(prev)-1)] + [1]
        res.append(row)
    return res
```

**Time:** O(n²)  
**Space:** O(n²)  

---

# 2. Using Only Index Access (Best for coding interviews)
## Step-by-Step approach:
1. **Initialize the result list**
   * Start with an empty list `res` to store all rows of Pascal’s Triangle.
     > This will hold the final output.

2. **Loop through `i` from 0 to `n-1`**
   * For each row, create a list `row` of size `i+1` filled with 1s.
     > This gives the basic structure with 1s at both ends.

3. **Fill inner values using previous row**
   * For every `j` from 1 to `i-1`, update `row[j]` as `res[i-1][j-1] + res[i-1][j]`.
     > This computes the value based on the sum of the two numbers directly above.

4. **Append the constructed row to result**
   * Add the completed `row` to `res`.
     > This builds the triangle row by row.

5. **Return the final triangle**
   * Use `return res` to output the full Pascal’s Triangle.

```python
def pt(n):
    res = []
    for i in range(n):
        row = [1]*(i+1)
        for j in range(1, i):
            row[j] = res[i-1][j-1] + res[i-1][j]
        res.append(row)
    return res
```

**Time:** O(n²)  
**Space:** O(n²)  

---

# 3. Recursive (Top-down)
## Step-by-Step approach:
1. **Define a recursive function `build(r)`**
   * Base case: if `r == 1`, return `[[1]]`
     > This initializes the triangle with the first row.

2. **Recursively build the triangle up to row `r-1`**
   * Call `build(r-1)` to get the triangle till previous row
     > This builds from bottom-up recursively.

3. **Generate the current row using the last row**
   * Use `prev = t[-1]` to get the last row
   * Create `cur = [1] + [prev[i] + prev[i+1] for i in range(len(prev)-1)] + [1]`
     > This computes the current row based on the previous one.

4. **Append the new row to triangle**
   * Add `cur` to the result `t` using `t.append(cur)`
     > This extends the triangle step by step.

5. **Return the final triangle**
   * Use `return build(n)` to get the triangle with `n` rows.

```python
def pt(n):
    def build(r):
        if r == 1: return [[1]]
        t = build(r-1)
        prev = t[-1]
        cur = [1] + [prev[i]+prev[i+1] for i in range(len(prev)-1)] + [1]
        t.append(cur)
        return t
    return build(n)
```

**Time:** O(n²)  
**Space:** O(n² + recursion stack)  

---

# 4. Mathematical (Combinatorics / nCr)
## Step-by-Step approach:
1. **Use list comprehension to generate rows**
   * Loop through `i` from `0` to `n-1` → `for i in range(n)`
     > This gives the index of each row.

2. **For each row `i`, compute entries using combinations**
   * Loop through `j` from `0` to `i` → `for j in range(i+1)`
   * Use `comb(i, j)` to compute the value at position `j` in row `i`
     > This calculates the binomial coefficient C(i, j), which is the formula for Pascal’s Triangle.

3. **Return the full triangle**
   * Collect all the rows into a list and return it
     > `return [[comb(i, j) for j in range(i+1)] for i in range(n)]` gives the final triangle with `n` rows.

```python
from math import comb
def pt(n):
    return [[comb(i, j) for j in range(i+1)] for i in range(n)]
```

**Time:** O(n²)  
**Space:** O(n²)  

---

# 5. Generator Style
## Step-by-Step approach:
1. **Define a generator function `gen()`**
   * Initialize `row` as `[1]` which is the first row of Pascal’s Triangle
     > This sets the starting point.

2. **Yield the current `row` and update it for the next iteration**
   * Use `yield row` to output the current row
   * Update `row` to the next row by adding pairs of adjacent elements and padding with 1 at both ends:
     `row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]`
     > This creates the next row based on the previous one.

3. **Create a generator instance and extract `n` rows**
   * Call `g = gen()` to create the generator object
   * Use a list comprehension `[next(g) for _ in range(n)]` to get the first `n` rows from the generator and return them
     > This returns the full Pascal’s Triangle up to row `n`.

```python
def pt(n):
    def gen():
        row = [1]
        while True:
            yield row
            row = [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]
    g = gen()
    return [next(g) for _ in range(n)]
```

**Time:** O(n²)  
**Space:** O(n²)  

---

# 6. Using `collections.defaultdict` for fun (not required)
## Step-by-Step approach:
1. **Initialize a result list `res` and a defaultdict `d` for memoization**
   * `res` will store all rows of Pascal’s Triangle
   * `d` maps tuple `(i, j)` to the value at row `i` and position `j`
     > This helps store and reuse computed values efficiently.

2. **Iterate through each row index `i` from 0 to `n-1`**
   * For each row, create an empty list `row`
   * For each position `j` in the row:
     * If `j` is at the edge (`0` or `i`), set `d[(i,j)] = 1` (edges are always 1)
     * Else calculate `d[(i,j)]` as the sum of the two values above: `d[(i-1,j-1)] + d[(i-1,j)]`
     * Append `d[(i,j)]` to the current `row`
     > This builds each row based on the previous row values using dynamic programming.

3. **Append the fully built `row` to `res`**
   * After completing each row, add it to the result list
     > This gradually forms the full Pascal’s Triangle.

4. **Return the result list `res` after all rows are generated**

```python
from collections import defaultdict
def pt(n):
    res = []
    d = defaultdict(int)
    for i in range(n):
        row = []
        for j in range(i+1):
            d[(i,j)] = 1 if j==0 or j==i else d[(i-1,j-1)] + d[(i-1,j)]
            row.append(d[(i,j)])
        res.append(row)
    return res
```

**Time:** O(n²)  
**Space:** O(n²)  

---

# 7. Numpy (not recommended for Leetcode, but possible)
## Step-by-Step approach:
1. **Initialize `res` as an empty list and `cur` as a NumPy array containing \[1]**
   * `res` will hold all rows of Pascal’s Triangle
   * `cur` represents the current row being generated, starting with the first row \[1].

2. **Iterate `n` times to build each row**
   * Append the current row `cur` converted to a list into `res`
   * Update `cur` by padding it with zeros on both ends using `np.pad`, then add the shifted arrays element-wise:
     * `np.pad(cur, (1,1), 'constant')[:-1]` shifts `cur` right by one
     * `np.pad(cur, (1,1), 'constant')[1:]` shifts `cur` left by one
     > Adding these creates the next row by summing adjacent elements of the current row.

3. **Return `res` after all rows are generated**
   * This gives the full Pascal’s Triangle up to `n` rows.

```python
import numpy as np
def pt(n):
    res = []
    cur = np.array([1])
    for _ in range(n):
        res.append(cur.tolist())
        cur = np.pad(cur, (1,1), 'constant')[:-1] + np.pad(cur, (1,1), 'constant')[1:]
    return res
```

**Time:** O(n²)  
**Space:** O(n²)  
