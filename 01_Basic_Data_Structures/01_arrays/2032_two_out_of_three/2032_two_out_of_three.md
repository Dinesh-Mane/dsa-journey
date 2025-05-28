# [2032. Two Out of Three](https://leetcode.com/problems/two-out-of-three/description/?envType=problem-list-v2&envId=hash-table)
## Problem Statement
Given three integer arrays `nums1`, `nums2`, and `nums3`, return a **distinct** array containing all the values that are **present in at least two** out of the three arrays. You may return the values in any order.

---

## ✅ Examples

```
Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]

Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]

Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
```

---

## Solution 1: Brute Force with Count Checks

**Idea**: Iterate through all unique elements and manually count how many arrays each appears in.

```python
def twoOutOfThree(nums1, nums2, nums3):
    result = []
    all_nums = set(nums1 + nums2 + nums3)
    for num in all_nums:
        count = 0
        if num in nums1:
            count += 1
        if num in nums2:
            count += 1
        if num in nums3:
            count += 1
        if count >= 2:
            result.append(num)
    return result
```

- **Time:** O(n) 
- **Space:** O(n)
- Simple but not the cleanest

---

## Solution 2: Use Sets for Fast Membership Checks

```python
def twoOutOfThree(nums1, nums2, nums3):
    set1, set2, set3 = set(nums1), set(nums2), set(nums3)
    all_nums = set1 | set2 | set3
    result = []
    for num in all_nums:
        count = (num in set1) + (num in set2) + (num in set3)
        if count >= 2:
            result.append(num)
    return result
```
```python
s1,s2,s3 = set(nums1), set(nums2), set(nums3)
all_nums = s1 | s2 | s3
res = []
for n in all_nums:
  if sum(n in s for s in (s1,s2,s3))>=2: res.append(n)
return res
```
```python
s1,s2,s3 = set(nums1), set(nums2), set(nums3)
all_nums = s1 | s2 | s3
res = [n for n in all_nums if sum(n in s for s in (s1, s2, s3)) >= 2]
return res
```
- **Time:** O(n)
- **Space:** O(n)
- ✅ Cleaner, faster due to `set` lookup

---

## Solution 3: Counter-based (Frequency from Each Array)

```python
from collections import defaultdict

def twoOutOfThree(nums1, nums2, nums3):
    seen = defaultdict(set)
    for num in set(nums1):
        seen[num].add(1)
    for num in set(nums2):
        seen[num].add(2)
    for num in set(nums3):
        seen[num].add(3)
    return [num for num, sources in seen.items() if len(sources) >= 2]
```

- **Time:** O(n)
- **Space:** O(n)
- ✅ Elegant and scalable

---

## Solution 4: Bitmask Encoding

```python
def twoOutOfThree(nums1, nums2, nums3):
    bits = {}
    for num in set(nums1):
        bits[num] = bits.get(num, 0) | 1
    for num in set(nums2):
        bits[num] = bits.get(num, 0) | 2
    for num in set(nums3):
        bits[num] = bits.get(num, 0) | 4
    return [num for num, mask in bits.items() if bin(mask).count('1') >= 2]
```

- **Time:** O(n)
- **Space:** O(n)
- ✅ Bitwise logic shows strong grasp of binary operations

---

## Optimal Solution (Recommended for Interviews)
**Solution 2 (Set-based)** and **Solution 3 (Dict-of-sets)** are both excellent.
- Efficient
- Easy to implement
- Good for real-time problem solving

---

## Hints for Solving Similar Problems
1. **Use sets** for fast presence checks.
2. **Count appearances per array**.
3. Use **defaultdict/set** when needing multi-array tracking.
4. Always consider **bitmasking** for compact source tracking.