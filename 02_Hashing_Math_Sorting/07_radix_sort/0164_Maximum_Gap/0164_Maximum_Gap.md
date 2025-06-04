# [164. Maximum Gap](https://leetcode.com/problems/maximum-gap/)
## Problem Statement
Given an integer array `nums`, return the maximum difference between two successive elements in its sorted form.
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

## Examples:
```
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form is [1,3,6,9]; maximum gap is max(3-1, 6-3, 9-6) = 3

Input: nums = [10]
Output: 0
```


# Sol 1(a). Sort + Linear Scan
## step-by-step approach:

1. Sort the array.
2. Loop over consecutive elements and compute the differences.
3. Return the max difference.

```python
def maximumGap(nums):
    if len(nums) < 2: return 0
    nums.sort()
    return max(nums[i] - nums[i - 1] for i in range(1, len(nums)))
```
Time: O(n log n)  
Space: O(1)   

# Sol 1(b). Using Sorted + Zip (Pythonic)
```python
def maximumGap(nums):
    if len(nums) < 2: return 0
    nums.sort()
    return max(b - a for a, b in zip(nums, nums[1:]))
```
Time: O(n log n)  
Space: O(1)  

# Sol 1(c). One-liner with Sorted
```python
def maximumGap(nums):
    return max(b - a for a, b in zip(sorted(nums), sorted(nums)[1:])) if len(nums) > 1 else 0
```
Time: O(n log n)  
Space: O(n)  

# Sol 1(d). Sorted + map + lambda
```python
def maximumGap(nums):
    if len(nums) < 2: return 0
    nums.sort()
    return max(map(lambda i: nums[i+1] - nums[i], range(len(nums)-1)))
```
Time: O(n log n)  
Space: O(1)  

---

# Sol 2. Radix Sort + Linear Scan
> ✅ Meets linear time + space requirement
> Radix sort the array, then scan for max gap.

## step-by-step approach:

1. Apply Radix Sort to sort the array in linear time.
2. Scan the sorted array and compute max difference between consecutive elements.
3. Return the maximum gap.

```python
def maximumGap(nums):
    if len(nums) < 2:
        return 0

    def radix_sort(arr):
        max_num = max(arr)
        exp = 1
        base = 10
        while max_num // exp > 0:
            buckets = [[] for _ in range(base)]
            for num in arr:
                buckets[(num // exp) % base].append(num)
            arr = [num for bucket in buckets for num in bucket]
            exp *= base
        return arr

    nums = radix_sort(nums)
    max_gap = 0
    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i - 1])
    return max_gap
```
Time: O(n)  
Space: O(n)  
> Best for interviews requiring linear time constraint

---

# Sol 3. Bucket Sort (Pigeonhole Principle)
> Best for interviews

**Idea:** Max gap ≥ bucket size → No two elements within a bucket will give the answer.  

## step-by-step approach:
1. Compute `min_val`, `max_val`, and number of buckets `n-1`.
2. Compute ideal bucket size = ceil((max - min) / (n - 1))
3. For each number, place it in a bucket storing only the min and max.
4. Max gap will be the max difference between `min_of_curr_bucket - max_of_prev_bucket`.

```python
def maximumGap(nums):
    if len(nums) < 2:
        return 0

    min_val, max_val = min(nums), max(nums)
    if min_val == max_val:
        return 0

    n = len(nums)
    bucket_size = max(1, (max_val - min_val) // (n - 1))
    bucket_count = ((max_val - min_val) // bucket_size) + 1

    buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

    for num in nums:
        idx = (num - min_val) // bucket_size
        buckets[idx][0] = min(buckets[idx][0], num)
        buckets[idx][1] = max(buckets[idx][1], num)

    prev_max = min_val
    max_gap = 0
    for i in range(bucket_count):
        if buckets[i][0] == float('inf'):
            continue
        max_gap = max(max_gap, buckets[i][0] - prev_max)
        prev_max = buckets[i][1]

    return max_gap
```

Time: O(n)  
Space: O(n)   

---

# Sol 4. Counting Sort (if value range is small)
> ✅ Linear time but only works if value range is small (e.g., 0 ≤ nums[i] ≤ 100000)

## step-by-step approach:

1. If < 2 elements, return `0`.
2. Build a presence array (`count[]`) marking which numbers exist.
3. Traverse `count[]`:
    - For each present number `i`, calculate `i - prev`.
    - Track the maximum gap between successive numbers.
4. Return the maximum gap.

```python
def maximumGap(nums):
    if len(nums) < 2:
        return 0
    count = [0] * (max(nums) + 1)
    for num in nums:
        count[num] = 1
    prev = -1
    max_gap = 0
    for i in range(len(count)):
        if count[i]:
            if prev != -1:
                max_gap = max(max_gap, i - prev)
            prev = i
    return max_gap
```
Time: O(n + m), where m = max(nums)  
Space: O(m)   

---

# Sol 5. Heap

## step-by-step approach:

1. Check edge case: If fewer than 2 elements, return `0`.
2. Heapify: Convert the array into a min-heap (sorted access one by one).
3. Pop min element: Start with the smallest value (`prev`).
4. Iterate through heap:
    - Pop each next smallest value (`curr`).
    - Compute `curr - prev` and update `max_gap`.
    - Set `prev = curr` for the next step.
5. Return the maximum gap found.

```python
import heapq
def maximumGap(nums):
    if len(nums) < 2:
        return 0
    heapq.heapify(nums)
    prev = heapq.heappop(nums)
    max_gap = 0
    while nums:
        curr = heapq.heappop(nums)
        max_gap = max(max_gap, curr - prev)
        prev = curr
    return max_gap
```
Time: O(n log n) — because heapq.heappop() is O(log n) and done n times.  
Space: O(1) extra (in-place heapify), but still doesn’t meet the problem’s O(n) time constraint.   

---

| Approach                     | Time       | Space    | Meets Linear Req?     | Notes                     |
| ---------------------------- | ---------- | -------- | --------------------- | ------------------------- |
| Radix Sort + Linear Scan     | O(n)       | O(n)     | ✅ Yes                 | Interview friendly        |
| **Bucket Sort (Pigeonhole)** | **O(n)**   | **O(n)** | ✅ Yes                 | **Best overall**          |
| Sorting + Linear Scan        | O(n log n) | O(1)     | ❌ No                  | Simple brute-force        |
| Counting Sort (if range ok)  | O(n + k)   | O(k)     | ✅ Yes (range-limited) | Use if max(nums) is small |
| Heap-based approach          | O(n log n) | O(n)     | ❌ No                  | Avoid                     |

