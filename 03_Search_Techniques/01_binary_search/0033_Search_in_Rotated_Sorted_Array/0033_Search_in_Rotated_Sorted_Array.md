# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Problem Statement

Given a rotated sorted array of distinct integers `nums` and a target value `target`, return its index if it is in the array, or `-1` if it is not.
You must write an algorithm with `O(log n)` runtime complexity.

---

## Examples:

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
```

---

# Sol 1. Modified Binary Search
## step-by-step approach:
* At each step:

  * Check if `nums[mid] == target` → return index.
  * Determine which half is **sorted**:

    * If **left half is sorted** (`nums[l] <= nums[mid]`):

      * Check if `target` lies in that half → move `r`.
      * Else → move `l`.
    * Else → right half is sorted:

      * Check if `target` lies in that half → move `l`.
      * Else → move `r`.
* Repeat until found or search space is empty.

```python
def search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target: return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]: r = mid - 1
            else: l = mid + 1
        else:
            if nums[mid] < target <= nums[r]: l = mid + 1
            else: r = mid - 1
    return -1
```

**Time:** O(log n)  
**Space:** O(1)  

---

# Sol 2. Find Pivot + Binary Search

## step-by-step approach:
* **Step 1:** Find the **pivot** (index of smallest element) using binary search → this is where the rotation occurred.
* **Step 2:** Decide which half to search:

  * If `target` lies in the range `[pivot, end]`, search there.
  * Else, search in `[start, pivot - 1]`.
* **Step 3:** Perform standard binary search in the chosen half.

> This splits the problem into **finding the rotation point** and then doing **binary search**, all in **O(log n)** time.


```python
def search(nums, target):
    def find_pivot():
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]: l = mid + 1
            else: r = mid
        return l

    def binary_search(l, r):
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            elif nums[m] < target: l = m + 1
            else: r = m - 1
        return -1

    if not nums: return -1
    pivot = find_pivot()
    if nums[pivot] <= target <= nums[-1]: return binary_search(pivot, len(nums) - 1)
    return binary_search(0, pivot - 1)
```

**Time:** O(log n)  
**Space:** O(1)  

---

# Sol 3. One-Liner Index (Brute Force)

## step-by-step approach:

* Directly check if `target` exists in `nums` using `in`.
* If found, return its index using `nums.index(target)`.
* Else, return `-1`.

> **Time Complexity:** O(n) — not optimal for large arrays.
> Used **Python built-in functions** instead of binary search.

```python
def search(nums, target):
    return nums.index(target) if target in nums else -1
```

**Time:** O(n)  
**Space:** O(1)  

---

# Sol 4. Recursive Binary Search

## step-by-step approach:

* This is a **recursive binary search** on a rotated sorted array.
* At each recursive call:

  * Check if `nums[mid] == target` → return index.
  * Determine which half is sorted.
  * Recursively search the sorted or unsorted half based on `target`.


> Same logic as iterative version, but done **recursively**.


```python
def search(nums, target):
    def helper(l, r):
        if l > r: return -1
        mid = (l + r) // 2
        if nums[mid] == target: return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]: return helper(l, mid - 1)
            else: return helper(mid + 1, r)
        else:
            if nums[mid] < target <= nums[r]: return helper(mid + 1, r)
            else: return helper(l, mid - 1)
    return helper(0, len(nums) - 1)
```

**Time:** O(log n)  
**Space:** O(log n) (recursion stack)  

---

# Sol 5. Modified Binary Search using while-else

## step-by-step approach:

* Performed **iterative binary search** on a rotated sorted array.
* At each step:

  * Check if middle element `nums[m]` is the `target`.
  * Determine if **left half is sorted**:

    * If so, check if `target` lies in that half → adjust `r`, else adjust `l`.
  * If right half is sorted, do similar check and adjust pointers.
* Loop ends when target is found or search space is exhausted.

> Same as earlier iterative version, but includes a clean `else` after the loop for `return -1`.

```python
def search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target: return m
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]: r = m - 1
            else: l = m + 1
        else:
            if nums[m] < target <= nums[r]: l = m + 1
            else: r = m - 1
    else: return -1
```

**Time:** O(log n)  
**Space:** O(1)  

---

# Sol 6. Ternary-Like Binary Search (Alternative style)

## step-by-step approach:

* Performed **iterative binary search** on a rotated sorted array.
* At each step:

  * Check if `nums[m]` is the target.
  * Use a **boolean flag `left_sorted`** to clearly indicate if the left half is sorted.
  * Based on this flag:

    * If left is sorted, check if `target` lies in that half → adjust `r`, else `l`.
    * If right is sorted, do the same check and update pointers accordingly.

> Same logic as standard rotated binary search, but made more **readable** using the `left_sorted` flag.

```python
def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target: return m
        left_sorted = nums[l] <= nums[m]
        if left_sorted:
            if nums[l] <= target < nums[m]: r = m - 1
            else: l = m + 1
        else:
            if nums[m] < target <= nums[r]: l = m + 1
            else: r = m - 1
    return -1
```

**Time:** O(log n)  
**Space:** O(1)  

---

# Sol 7. Find Pivot Index First Then Search

## step-by-step approach:

* **Step 1: Find Pivot**
  * Used binary search to find the **rotation index** (smallest element), where array was rotated.

* **Step 2: Decide Search Range**
  * If `target ≥ nums[0]`, it lies in the **left sorted part** → search `[0, pivot - 1]`.
  * Else, search the **right sorted part** → `[pivot, n - 1]`.

* **Step 3: Binary Search**
  * Performed standard binary search in the chosen half.

> Clean **pivot-based binary search** with clear range partitioning.

```python
def search(nums, target):
    def find_pivot(nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]: l = mid + 1
            else:r = mid
        return l

    if not nums: return -1

    n = len(nums)
    pivot = find_pivot(nums)

    l, r = (0, pivot - 1) if target >= nums[0] else (pivot, n - 1)
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target: return m
        elif nums[m] < target: l = m + 1
        else: r = m - 1
    return -1
```

**Time:** O(log n)  
**Space:** O(1)  

---

### Summary Table

| Solution                      | Time     | Space    | Type               |
| ----------------------------- | -------- | -------- | ------------------ |
| Modified Binary Search        | O(log n) | O(1)     | ✅ Optimal          |
| Pivot + Binary Search         | O(log n) | O(1)     | Clean, clear       |
| Brute Force (index/in)        | O(n)     | O(1)     | Not accepted       |
| Recursive Binary Search       | O(log n) | O(log n) | Recursion version  |
| While-Else Modified Binary    | O(log n) | O(1)     | Pythonic variation |
| Ternary Style Binary          | O(log n) | O(1)     | Logical variant    |
| Find Pivot First, Then Search | O(log n) | O(1)     | Two-phase search   |

