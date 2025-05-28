# [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/description/)
## Problem Statement:
You are given an array of intervals, where each interval is represented as [start, end]. Some of these intervals might overlap. Your task is to merge all overlapping intervals into one and return an array of the merged non-overlapping intervals that cover all the original intervals.

## Examples
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping
```

# Possible solutions:
# Sol 1: Sort + Merge (Greedy)
## ✅ Core Idea
1. Sort the intervals by their start value.
2. Start with the first interval and try to merge any overlapping intervals.
3. If the current interval's start `s` is less than or equal to the end of the last interval in result `res[-1][1]`, they overlap.
4. In that case, extend the end of the last interval to `max(res[-1][1], e)`.
5. If not overlapping, just add the new interval.

```python
class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort()
        res = [a[0]]
        for s, e in a[1:]:
            if s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
        return res
```
Time: O(n log n) (due to sorting)  
Space: O(n) (for output)  

# Sol 2: Sort + In-place Merge
This is an in-place optimized version of the greedy merge approach. It avoids creating a separate list to store the results by directly updating the input list `a`.

## Step-by-Step Logic
1. Sort intervals based on start time (just like in Sol 1).
2. Initialize index `i = 0` to point to the last merged interval.
3. Loop through the array with index `j` from 1 to n-1:
    - If a[j] overlaps with `a[i]` → merge: update `a[i][1]`
    - If not → move i forward and place a[j] at a[i]
4. Return the list up to index `i+1`.

```python
class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort()
        i = 0
        for j in range(1, len(a)):
            if a[j][0] <= a[i][1]:
                a[i][1] = max(a[i][1], a[j][1])
            else:
                i += 1
                a[i] = a[j]
        return a[:i+1]
```
Time: O(n log n)  
Space: O(1) (in-place merge, ignoring sort output space)  

---

### Recommended in Interviews:
- Use Sol 1 for clarity and standard correctness.
- Use Sol 2 if the interviewer wants space-optimized or in-place solutions.

---

# Sol 3: Heap (less optimal for merging, but possible)
This solution uses a min-heap to manage the merging of intervals. It’s an alternative approach, but less optimal compared to the greedy in-place method.

## Step-by-Step Logic
1. Sort the intervals by their start times.
2. Initialize a min-heap (`h`) to store merged intervals.
3. Loop through each interval `[s, e]`:
    - If the heap is empty or current `[s, e]` does not overlap with the smallest (top of heap), push it as a new interval.
    - If it overlaps, pop the top interval, merge it with current, and push back the merged result.
4. Finally, return the sorted heap for a clean output

```python
import heapq
class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort()
        h = []
        for s, e in a:
            if not h or h[0][0] > e:
                heapq.heappush(h, [s, e])
            else:
                t = heapq.heappop(h)
                heapq.heappush(h, [min(s, t[0]), max(e, t[1])])
        return sorted(h)
```
Time: O(n log n)  
Space: O(n) (for heap)  

# Sol 4: Custom Stack
Use a stack to keep track of merged intervals as you iterate through the sorted list of intervals.

## Step-by-Step Logic
1. Sort the intervals by start time.
2. Initialize an empty stack (`stk`).
3. Iterate over each interval `[s, e]`:
    - If stack is not empty and the end of the last interval on stack overlaps with the current start (`stk[-1][1] >= s`), merge by updating the end of the last interval with the max end.
    - Otherwise, push the current interval onto the stack
4. Return the stack which now contains merged non-overlapping intervals.

```python
class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort()
        stk = []
        for s, e in a:
            if stk and stk[-1][1] >= s:
                stk[-1][1] = max(stk[-1][1], e)
            else:
                stk.append([s, e])
        return stk
```
Time: O(n log n)  
Space: O(n) (for stack)  

