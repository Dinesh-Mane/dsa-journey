# [2006. Count Number of Pairs With Absolute Difference K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/?envType=problem-list-v2&envId=hash-table)

Given an array of integers `nums` and an integer `k`, return the number of pairs `(i, j)` where `i < j` and `|nums[i] - nums[j]| == k`.
### Absolute difference:
`|a - b|` means the distance between `a` and `b` on the number line.

---

### ✅ Examples:

**Example 1:**
```python
Input: nums = [1,2,2,1], k = 1
Output: 4
# Explanation: 4 pairs have a difference of 1

Input: nums = [1,3], k = 3
Output: 0
# No pair with difference of 3

Input: nums = [3,2,1,5,4], k = 2
Output: 3
# Pairs: (3,1), (2,4), (1,3)
```

---

## ✅ Solution 1: Brute Force

**Idea:**
Check every pair `(i, j)` with `i < j` and count if `|nums[i] - nums[j]| == k`.

```python
def countKDifference(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                count += 1
    return count
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

---

## ✅ Solution 2: HashMap Frequency Count

**Idea:**
Count how many times each number appears. For each `num`, check how many `num - k` and `num + k` exist in the map.

```python
from collections import Counter

def countKDifference(nums, k):
    count = 0
    freq = Counter(nums)
    for num in freq:
        count += freq[num] * freq.get(num - k, 0)
    return count
```

**Note:** This checks only one side (i > j), but you can do `num + k` or `num - k`, not both.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## ✅ Solution 3: HashMap with Online Update

**Idea:**
While iterating over `nums`, for each `num`, check how many times `num - k` and `num + k` have occurred **before**.

```python
from collections import defaultdict

def countKDifference(nums, k):
    count = 0
    freq = defaultdict(int)
    for num in nums:
        count += freq[num - k] + freq[num + k]
        freq[num] += 1
    return count
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

✅ Cleaner than previous, works well for interviews.

---

## ✅ Solution 4: Sorting with Two Pointers (Not Optimal Here)

**Idea:**
Sort and use two pointers to find pairs with a diff of `k`.

```python
def countKDifference(nums, k):
    nums.sort()
    count = 0
    left = 0
    for right in range(1, len(nums)):
        while nums[right] - nums[left] > k:
            left += 1
        if nums[right] - nums[left] == k:
            count += 1
    return count
```

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1) or O(n) depending on sort

⚠️ May not count all valid pairs correctly if duplicates exist — not recommended for this problem.

---

## ✅ Summary Table

| Approach                         | Time     | Space   | Notes                              |
|----------------------------------|----------|---------|------------------------------------|
| Brute Force                     | O(n²)    | O(1)    | ❌ Too slow                         |
| HashMap Frequency (Method 1)   | O(n)     | O(n)    | ✅ Efficient and readable           |
| HashMap Running Count (Method 2)| O(n)     | O(n)    | ✅✅ Optimal for interviews          |
| Two Pointers (Sorted)          | O(n log n)| O(1)    | ⚠️ Not reliable with duplicates     |

---

## 💡 Hints for Solving Such Questions:

1. Ask if order matters: Is `(i, j)` the same as `(j, i)`?
2. If difference or sum is involved → HashMap is often optimal.
3. When using `abs`, always try both `num + k` and `num - k`.
4. Watch for constraints: if `1 <= nums[i] <= 100`, you can even use a frequency array of size 101.

---

## 💬 Best Solution for Interviews:

✅ **Solution 3 (HashMap with Online Count)** is best:
* One pass
* Clean logic
* Easy to explain
* Optimal time and space