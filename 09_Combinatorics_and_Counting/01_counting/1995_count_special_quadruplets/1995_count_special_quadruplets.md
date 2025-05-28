# [1995. Count Special Quadruplets](https://leetcode.com/problems/count-special-quadruplets/description/?envType=problem-list-v2&envId=hash-table)

## Problem Statement
Given a **0-indexed** integer array `nums`, return the number of **distinct quadruplets** `(a, b, c, d)` such that:

- `nums[a] + nums[b] + nums[c] == nums[d]`, and
- `a < b < c < d`

---

## Examples

### Example 1
```
Input: nums = [1,2,3,6]
Output: 1
Explanation: 1 + 2 + 3 == 6 → (0,1,2,3)
```

### Example 2
```
Input: nums = [3,3,6,4,5]
Output: 0
Explanation: No valid quadruplet exists.
```

### Example 3
```
Input: nums = [1,1,1,3,5]
Output: 4
Explanation:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5
```

---

## Solution 1: Brute Force (4 Nested Loops)

**Idea**: Try every possible combination where `a < b < c < d` and check if condition holds.

```python
def countQuadruplets(nums):
    n = len(nums)
    count = 0
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    if nums[a] + nums[b] + nums[c] == nums[d]:
                        count += 1
    return count
```

- **Time:** O(n⁴)
- **Space:** O(1)
- ❌ Inefficient for larger inputs (n up to 50)

---

## Solution 2: Fix `d`, Precompute Triplet Sums

**Idea**: For every `d`, look for triplets `(a,b,c)` such that sum = `nums[d]`

```python
def countQuadruplets(nums):
    n = len(nums)
    count = 0
    for d in range(3, n):
        for a in range(d):
            for b in range(a+1, d):
                for c in range(b+1, d):
                    if nums[a] + nums[b] + nums[c] == nums[d]:
                        count += 1
    return count
```

- **Time:** O(n⁴) worst-case, but practically faster (fewer iterations)
- **Space:** O(1)
- ⚠️ Slight improvement in runtime

---

## Solution 3: Cleaned O(n³) without Redundant HashMap

**Idea**: Fix `c` and `d`, compute target = `nums[d] - nums[c]`, check if any `a < b < c` satisfy `nums[a] + nums[b] == target`

```python
def countQuadruplets(nums):
    n = len(nums)
    count = 0
    for c in range(2, n-1):
        for d in range(c+1, n):
            target = nums[d] - nums[c]
            for a in range(c):
                for b in range(a+1, c):
                    if nums[a] + nums[b] == target:
                        count += 1
    return count
```

- **Time:** O(n³)
- **Space:** O(1)
- ✅ Much faster than brute-force and simpler

---

## Solution 4: Optimized HashMap with Frequency Table

**Idea**: Iterate `d` from end, track counts of `nums[d] - nums[c]`, then check against earlier pairs.

```python
from collections import defaultdict

def countQuadruplets(nums):
    n = len(nums)
    count = 0
    freq = defaultdict(int)
    for b in range(n-3, -1, -1):
        for d in range(b+2, n):
            diff = nums[d] - nums[b+1]
            freq[diff] += 1
        for a in range(b):
            total = nums[a] + nums[b]
            count += freq[total]
    return count
```

- **Time:** O(n²)
- **Space:** O(n)
- ✅✅ **Best approach** – highly efficient
- ✅ Suitable for **interviews**

---

## Hints to Solve These Problems

1. **Look for fixed variables**:
   - Fix `d`, check combinations before it.
2. **Use hashmap for reverse lookup**:
   - `sum == nums[d]` ⇒ use `target = nums[d] - (x + y)`
3. **Avoid duplicate work**:
   - HashMaps help avoid re-computing sums
4. **Try different loop orders**:
   - Start from the end if looking forward is difficult

---

## ✅ Best for Interviews
**Solution 4: Optimized HashMap with Frequency Table** is:
- Clean
- Scalable
- Uses efficient time-space tradeoffs
- Demonstrates good problem-solving thinking
