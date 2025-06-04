# [704. Binary Search](https://leetcode.com/problems/binary-search/description/)

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

## Examples:
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

---

# 1. Iterative Binary Search (Standard)

## step-by-step approach:

* Start with two pointers: `l` (left) and `r` (right).
* Repeatedly calculate the middle index `m`.
* If `nums[m] == target`, return `m`.
* If `nums[m] < target`, search in the **right half** by updating `l = m + 1`.
* If `nums[m] > target`, search in the **left half** by updating `r = m - 1`.
* If not found, return `-1`.

> Efficiently halves the search space each time.

```python
def search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target: return m
        elif nums[m] < target: l = m + 1
        else: r = m - 1
    return -1
```

**Time:** O(log n), **Space:** O(1)

---

# 2. Recursive Binary Search

## step-by-step approach:

* Define a helper function `binary(l, r)` to perform recursion.
* Base case: if `l > r`, return `-1` (target not found).
* Calculate `m = (l + r) // 2`.
* If `nums[m] == target`, return `m`.
* If `nums[m] < target`, recurse on the **right half** → `binary(m + 1, r)`.
* If `nums[m] > target`, recurse on the **left half** → `binary(l, m - 1)`.


```python
def search(nums, target):
    def binary(l, r):
        if l > r: return -1
        m = (l + r) // 2
        if nums[m] == target: return m
        elif nums[m] < target: return binary(m + 1, r)
        else: return binary(l, m - 1)
    return binary(0, len(nums) - 1)
```

**Time:** O(log n), **Space:** O(log n) (due to recursion stack)

---

# 3. Using Python’s `bisect` module

## step-by-step approach:

* `bisect_left(nums, target)` finds the leftmost position `i` where `target` can be inserted to keep `nums` sorted.
* If `i` is within bounds and `nums[i] == target`, return `i`.
* Else, return `-1` (target not found).


```python
import bisect
def search(nums, target):
    i = bisect.bisect_left(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
```

**Time:** O(log n), **Space:** O(1)

---

# 4. One-liner with `try` and `.index()` (Not O(log n), but compact)
## step-by-step approach:
* `nums.index(target)` returns the index if `target` exists.
* If not, it raises a `ValueError`, so `except` handles it and returns `-1`.

```python
def search(nums, target):
    try: return nums.index(target)
    except: return -1
```

**Time:** O(n), **Space:** O(1) ❌ (*not acceptable in strict O(log n)*)

---

# 5. Iterative with mid calc optimized
## step-by-step approach:
**Summary:**
Used **iterative binary search** to find the `target`:

* Set `l` (left) and `r` (right) pointers at start and end.
* Calculate middle index `m = l + (r - l) // 2` to avoid overflow.
* If `nums[m] == target`, return `m`.
* If `nums[m] < target`, search in right half (`l = m + 1`).
* Else, search in left half (`r = m - 1`).
* If not found, return `-1`.

```python
def search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target: return m
        if nums[m] < target: l = m + 1
        else: r = m - 1
    return -1
```

**Time:** O(log n), **Space:** O(1)

---

# 6. Iterative with `for` loop instead of `while`
## step-by-step approach:

* You loop `len(nums)` times (maximum possible), but exit early if `l > r`.
* Each time:
  * Calculate the middle index `m`.
  * If `nums[m] == target`, return `m`.
  * If target is greater, search the right half.
  * If target is smaller, search the left half.
* Return `-1` if the target is not found.

> Using `for` instead of `while` is unconventional for binary search, but logically works. Use `while` in interviews for clarity.

```python
def search(nums, target):
    l, r = 0, len(nums)-1
    for _ in range(len(nums)):
        if l > r: break
        m = (l + r) // 2
        if nums[m] == target: return m
        elif nums[m] < target: l = m + 1
        else: r = m - 1
    return -1
```

**Time:** O(log n), **Space:** O(1)

---

# 7. Iterative Binary with `match-case` (Python 3.10+)
## step-by-step approach:
* Set `l` and `r` as search bounds.
* Loop while `l <= r`:

  * Compute middle index `m`.
  * Use `match nums[m]` to:

    * Return `m` if `nums[m] == target`.
    * Narrow to right half if `nums[m] < target`.
    * Narrow to left half otherwise.
* Return `-1` if target not found.


```python
def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        match nums[m]:
            case _ if _ == target: return m
            case _ if _ < target: l = m + 1
            case _: r = m - 1
    return -1
```
> This version is functionally the same as the classic binary search but uses `match-case` from Python 3.10+ for more expressive logic. Stick to standard `if-elif-else` in interviews unless asked otherwise.

**Time:** O(log n), **Space:** O(1)

---

# 8. List comprehension trick (Inefficient, not interview-safe)
## step-by-step approach:
* Checked if `target` exists in `nums`.
* If yes, used list comprehension with `enumerate(nums)` to collect all indices where `x == target`, then returned the first one (`[0]`).
* If not, returned `-1`.

```python
def search(nums, target):
    return [i for i, x in enumerate(nums) if x == target][0] if target in nums else -1
```
**Time:** O(n), **Space:** O(n)  
> **Not suitable for interviews**—doesn't meet the O(log n) requirement. Use standard binary search instead.