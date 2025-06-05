# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)
You are climbing a staircase. It takes n steps to reach the top.  
Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?


## Example
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

---

# 1. Recursive (Naive)

## Step-by-Step approach:
1. **Check the base case**
   * **If `n` is 1 or 2**, immediately return `n`.
     * This is because:
       * `cs(1)` = 1 way → just one step.
       * `cs(2)` = 2 ways → \[1+1] or \[2].
         > This stops the recursion from going infinitely.

2. **Use recursion to break the problem down**
   * For any `n > 2`, calculate:
     * `cs(n-1)` → the number of ways to reach the `(n-1)`th step.
     * `cs(n-2)` → the number of ways to reach the `(n-2)`th step.
       > This works because you can either take 1 step from `(n-1)` or 2 steps from `(n-2)` to reach `n`.
3. **Add the results**
   * The total number of ways to reach step `n` is the **sum of ways to reach `(n-1)` and `(n-2)`**.
     > `cs(n) = cs(n-1) + cs(n-2)`

> This approach builds the solution using a **top-down recursive breakdown**, similar to computing the Fibonacci series, where each result depends on the previous two.

```python
def cs(n):
    if n <= 2: return n
    return cs(n-1) + cs(n-2)
```

**Time:** O(2ⁿ)  
**Space:** O(n) (call stack)  

---

# 2. Recursive + Memoization (Top-Down DP)

## Step-by-Step approach:
1. **Check if the result is already memoized**
   * If `n` is present in the dictionary `dp`, return `dp[n]`.
     * This avoids recomputing the result for the same input and significantly reduces time complexity.

     > This is the core idea of memoization—reuse previously computed results.

2. **Check the base case**
   * If `n` is 1 or 2, return `n`.
     * This is because:
       * `cs(1)` = 1 way → just one step.
       * `cs(2)` = 2 ways → \[1+1] or \[2].
     > These are the smallest subproblems and serve as the base of the recursion tree.

3. **Recursively calculate the result**
   * If `n` is not already memoized, compute it using:
     * `cs(n-1, dp)` → the number of ways to reach the `(n-1)`th step.
     * `cs(n-2, dp)` → the number of ways to reach the `(n-2)`th step.
   * Store the result in `dp[n] = cs(n-1, dp) + cs(n-2, dp)`.

4. **Return the memoized result**
   * Finally, return `dp[n]` which now holds the number of distinct ways to reach step `n`.

> This approach uses a **top-down recursive strategy with memoization**, making it efficient by avoiding redundant calculations through dynamic programming.

```python
def cs(n, dp={}):
    if n in dp: return dp[n]
    if n <= 2: return n
    dp[n] = cs(n-1, dp) + cs(n-2, dp)
    return dp[n]
```

**Time:** O(n)  
**Space:** O(n)  

---

# 3. Bottom-Up DP (Tabulation)

## Step-by-Step approach:
1. **Handle base cases**
   * If `n` is 1 or 2, immediately return `n`.
     * Because:
       * `cs(1)` = 1 way → just one step.
       * `cs(2)` = 2 ways → \[1+1], \[2].
     > These act as the foundation for building further results.

2. **Initialize a DP table**
   * Create a list `dp` of size `n+1` filled with 0.
   * Set `dp[1] = 1` and `dp[2] = 2` to represent known base cases.
     > This sets the starting point for the iterative calculation.

3. **Iteratively build the solution**
   * Loop from `i = 3` to `n`:
     * For each step `i`, calculate:
       `dp[i] = dp[i-1] + dp[i-2]`
       * Meaning: ways to reach step `i` is the sum of ways to reach step `i-1` and `i-2`.
     > This is based on the recurrence relation like Fibonacci numbers.

4. **Return the result**
   * Return `dp[n]`, which holds the number of ways to reach the top.

> This approach builds the answer from the ground up using **bottom-up dynamic programming**, eliminating recursion and optimizing both time and space.

```python
def cs(n):
    if n <= 2: return n
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

**Time:** O(n)  
**Space:** O(n)  

---

# 4. Bottom-Up DP (Space Optimized)
> Best Approach for Coding Interviews

## Step-by-Step approach:
1. **Handle base cases**
   * If `n` is 1 or 2, immediately return `n`.
     * Because:
       * `cs(1)` = 1 way → just one step.
       * `cs(2)` = 2 ways → \[1+1], \[2].
     > These are the base values needed to build further results.

2. **Initialize two variables for the first two steps**
   * Set `a = 1` (ways to reach step 1)
   * Set `b = 2` (ways to reach step 2)
     > These act like the first two entries of a Fibonacci sequence.

3. **Iteratively compute ways from step 3 to step n**
   * Loop from 3 to `n`:
     * In each iteration, update:
       * `a, b = b, a + b`
       * Meaning: shift `a` forward and set new `b` as the sum of the last two values.
     > This avoids using an array and only tracks the last two states.

4. **Return the result**
   * After the loop, return `b`, which now holds the number of ways to reach step `n`.

> This is a **bottom-up space-optimized dynamic programming** approach, reducing space complexity from O(n) to O(1).

```python
def cs(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b
```

**Time:** O(n)  
**Space:** O(1)  

---

# 5. Fibonacci Formula (Closed-form / Binet's Formula)

## Step-by-Step approach:
1. **Understand the relationship to Fibonacci**
   * The number of ways to climb `n` stairs is the same as computing the `(n+1)`th Fibonacci number.
     > Because each step depends on the two previous steps, just like the Fibonacci sequence.

2. **Use Binet’s Formula for Fibonacci numbers**
   * Binet’s Formula (closed-form) for the `k`th Fibonacci number:
     $$
     F(k) = \frac{{\phi^k - \psi^k}}{\sqrt{5}}
     $$
     where:
     * $\phi = \frac{{1 + \sqrt{5}}}{2}$ (Golden Ratio)
     * $\psi = \frac{{1 - \sqrt{5}}}{2} = -\frac{1}{\phi}$

3. **Substitute (n+1) into the formula**
   * You compute:
     $$
     F(n+1) = \frac{{\phi^{n+1} - (-1/\phi)^{n+1}}}{\sqrt{5}}
     $$
     > This gives the exact number of distinct ways to reach the top of the staircase.

4. **Round the result to handle floating-point errors**
   * Since floating-point calculations can be imprecise, you use `round()` to get the nearest integer.

5. **Return the final value**
   * This value represents the number of ways to climb `n` stairs using the closed-form expression.

> This approach is highly efficient with **time complexity O(1)** and **space complexity O(1)**, but relies on floating-point precision.

```python
from math import sqrt
def cs(n):
    phi = (1 + sqrt(5)) / 2
    return round((phi**(n+1) - (-1/phi)**(n+1)) / sqrt(5))
```

**Time:** O(1)  
**Space:** O(1)  

---

# 6. Using `lru_cache` Decorator

## Step-by-Step approach:
1. **Decorate the function with `@lru_cache(None)`**
   * This **automatically stores the results of previous function calls**.
   * `None` means it will cache an unlimited number of calls.
   > This avoids redundant computation, making recursion efficient.

2. **Check the base case**
   * **If `n` is 1 or 2**, directly return `n`.
     * Because:
       * `cs(1)` → 1 way (just one step)
       * `cs(2)` → 2 ways (1+1 or 2)
     > This halts the recursion at the simplest cases.

3. **Apply recursion to solve larger problems**
   * Compute `cs(n-1)` → number of ways to reach step `n-1`.
   * Compute `cs(n-2)` → number of ways to reach step `n-2`.
     > Because from either of those, you can reach `n` with one or two steps.

4. **Return the total**
   * Add the results of `cs(n-1)` and `cs(n-2)` to get total ways to climb `n` steps:
     $$
     cs(n) = cs(n-1) + cs(n-2)
     $$

> This approach is a **top-down recursion with memoization**, giving **time complexity O(n)** and **space complexity O(n)** (for the recursion stack and cache).

```python
from functools import lru_cache
@lru_cache(None)
def cs(n):
    if n <= 2: return n
    return cs(n-1) + cs(n-2)
```

**Time:** O(n)  
**Space:** O(n)  

---

# 7. Using Itertools (Generator for Fibonacci)

## Step-by-Step approach:
1. **Define a generator function `fib()`**
   * Start with `a = 1` and `b = 2`, which represent the number of ways to reach step 1 and step 2.
   * Use `while True` to yield an **infinite Fibonacci sequence**, where each value is the sum of the previous two.
     > This simulates the climbing steps as a Fibonacci progression.

2. **Use `itertools.islice` to skip directly to the (n-1)th Fibonacci number**
   * `islice(fib(), n-1, None)` creates an iterator starting at the `(n-1)`th term of the sequence.
     > Because the first Fibonacci term (`a = 1`) corresponds to `n = 1`, we want the (n-1)th term for `cs(n)`.

3. **Return the first value from the sliced generator**
   * `next(...)` fetches the desired Fibonacci number — the number of ways to reach step `n`.

> This is a **lazy evaluation** approach using generators.
> **Time complexity:** `O(n)`
> **Space complexity:** `O(1)` since it only stores two variables at a time.

```python
from itertools import islice
def cs(n):
    def fib(): a, b = 1, 2
        while True: yield a; a, b = b, a + b
    return next(islice(fib(), n-1, None))
```

**Time:** O(n)  
**Space:** O(1) (ignoring generator overhead)  

---

# 8. Using Matrix Exponentiation
## Step-by-Step Approach:

1. **Understand the relationship between Fibonacci numbers and climbing stairs**
   * The number of ways to climb `n` stairs follows the **Fibonacci sequence**:
     > `cs(n) = Fib(n+1)`
     > (since `Fib(1) = 1`, `Fib(2) = 1`, ... and `cs(1) = 1`, `cs(2) = 2`)

2. **Define a matrix multiplication function `mul(a, b)`**
   * Multiply two 2x2 matrices using the standard matrix multiplication rule.
     > This helps compute powers of the Fibonacci base matrix.

3. **Define a matrix exponentiation function `mat_pow(m, p)`**
   * Raise a matrix `m` to power `p` using **binary exponentiation** (also called exponentiation by squaring):
     * If `p` is odd, multiply the result matrix `res` by current matrix `m`.
     * Square `m` on each step and halve `p`.
     > This computes `m^p` efficiently in `O(log p)` time.

4. **Use matrix exponentiation to compute the nth Fibonacci number**
   * Raise the **Fibonacci base matrix** `[[1,1],[1,0]]` to power `n`:
     * The result will be a matrix where the top-left element (`[0][0]`) equals `Fib(n+1)`.
     > This directly gives you the number of ways to climb `n` stairs.

5. **Return the result**
   * Return `res[0][0]` — the top-left value of the exponentiated matrix, which gives you `cs(n)`.

> This is a highly optimized approach using **matrix exponentiation**.
> **Time Complexity:** `O(log n)`
> **Space Complexity:** `O(1)` (only constant-sized matrices are used)

```python
def cs(n):
    def mul(a, b):
        return [
            [a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]],
            [a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]],
        ]
    def mat_pow(m, p):
        res = [[1,0],[0,1]]
        while p:
            if p%2: res = mul(res, m)
            m = mul(m, m)
            p //= 2
        return res
    return mat_pow([[1,1],[1,0]], n)[0][0]
```

**Time:** O(log n)  
**Space:** O(log n) (recursion)  

---
