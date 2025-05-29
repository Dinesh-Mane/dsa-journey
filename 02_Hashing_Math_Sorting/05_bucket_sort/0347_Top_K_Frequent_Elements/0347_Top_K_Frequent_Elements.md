# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)
## Problem Statement:
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## Examples
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
```

# Possible solutions:
# Sol 1. Brute Force (Sorting by Frequency)
## ✅ Core Idea
1. Count the frequency of each element using `Counter`.
2. Sort the elements by frequency in descending order.
3. Return the first `k` elements from the sorted list.

```python
from collections import Counter
def topKFrequent(nums, k):
    c = Counter(nums)
    sorted_items = sorted(c.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_items[:k]]
```
OR
```python
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [x for x, _ in sorted(c.items(), key=lambda x: -x[1])[:k]]
```
Time: O(n log n) | Space: O(n)  

# Sol 2. Heap (Min-Heap of size k)

## Step-by-Step Logic
1. Use `Counter` to count frequencies of elements in `nums`.
2. Use `heapq.nlargest` to get `k` elements with highest frequencies.
3. Return only the element part (`x`) from the `(element, frequency)` pairs.

```python
from collections import Counter
import heapq

def topKFrequent(nums, k):
    c = Counter(nums)
    return [x for x, _ in heapq.nlargest(k, c.items(), key=lambda x: x[1])]
```
in `return [x for x, _ in heapq.nlargest(k, c.items(), key=lambda x: x[1])]`
- `c.items()` returns a list of tuples: (element, frequency).
- `heapq.nlargest(k, ...)` retrieves the `k` items with the highest frequencies.
- `key=lambda x: x[1]` tells it to sort by frequency.
- List comprehension extracts just the elements (`x`) from the `(element, frequency)` tuples.
- Example: For k = 2 → result = [1, 2]

Time: O(n log k) | Space: O(n)  


# Sol 3. Bucket Sort
> Best for coding interviews

## Step-by-Step Logic
1. Count frequencies using `Counter` or `defaultdict`.
2. Create buckets: Each index represents a frequency; store elements with that frequency.
3. Iterate from high to low frequency and collect elements until `k` most frequent are found.

```python
from collections import defaultdict

def topKFrequent(nums, k):
    freq_map = defaultdict(int)
    for n in nums:
        freq_map[n] += 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for n, f in freq_map.items():
        buckets[f].append(n)

    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for n in buckets[i]:
            res.append(n)
            if len(res) == k:
                return res
```
OR
```python
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        b = [[] for _ in range(len(nums)+1)]
        for x, f in c.items():
            b[f].append(x)
        res = []
        for i in range(len(b)-1, 0, -1):
            for x in b[i]:
                res.append(x)
                if len(res) == k:
                    return res
```
Time: O(n) | Space: O(n)  

---

# Sol 4: Manual HashMap + Heap
This is a very concise one-liner solution using Python’s built-in `sorted()` function with a custom lambda function to sort characters by frequency.

## Step-by-Step Logic
1. Build frequency map `m` for all elements in `nums`.
2. Maintain **min-heap** of size `k` using frequencies to keep top `k` frequent elements.
3. Extract and return the elements from the heap.

```python
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for x in nums:
            m[x] = m.get(x, 0) + 1
        h = []
        for x, f in m.items():
            heapq.heappush(h, (f, x))
            if len(h) > k:
                heapq.heappop(h)
        return [x for _, x in h]
```
In this code, the min-heap keeps track of the top k frequent elements by storing pairs (frequency, number).
- When a new element is pushed, if the heap size exceeds k, the smallest frequency element (the root of the min-heap) is popped out.
- This way, the heap always contains the k elements with the highest frequencies, because less frequent elements get removed first.
- At the end, the heap holds exactly the top k frequent numbers.

Time: O(n log k)  
Space: O(n)  


# Sol 5. Quickselect (Partition-based)
This is a very concise one-liner solution using Python’s built-in `sorted()` function with a custom lambda function to sort characters by frequency.

## Step-by-Step Logic
1. Count frequencies using `Counter`.
2. Use Quickselect to partially sort items by frequency, so top `k` frequent are in the first `k` positions.
3. Partition rearranges items around a pivot frequency, pushing higher frequencies left.
4. Recursively narrow search until top `k` are positioned.
5. Return the first `k` elements’ keys as result.

```python
from collections import Counter
import random

def topKFrequent(nums, k):
    count = Counter(nums)
    items = list(count.items())

    def partition(l, r, pivot_idx):
        pivot_freq = items[pivot_idx][1]
        items[pivot_idx], items[r] = items[r], items[pivot_idx]
        store_idx = l
        for i in range(l, r):
            if items[i][1] > pivot_freq:
                items[store_idx], items[i] = items[i], items[store_idx]
                store_idx += 1
        items[store_idx], items[r] = items[r], items[store_idx]
        return store_idx

    def quickselect(l, r, k):
        if l == r:
            return
        pivot_idx = random.randint(l, r)
        idx = partition(l, r, pivot_idx)
        if idx == k:
            return
        elif idx < k:
            quickselect(idx + 1, r, k)
        else:
            quickselect(l, idx - 1, k)

    quickselect(0, len(items) - 1, k)
    return [x[0] for x in items[:k]]
```
Time: O(n) average, O(n²) worst  
Space: O(n)  

