# [2359. Find Closest Node to Given Two Nodes](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/)
## Problem Statement

You are given a **directed graph** represented as an array `edges`, where each index `i` has **at most one outgoing edge** to `edges[i]`. If there is no outgoing edge, `edges[i] == -1`.

Given two nodes `node1` and `node2`, return the **index of the node** that is **reachable from both** and minimizes the **maximum distance** from either `node1` or `node2`.
If multiple such nodes exist, return the **smallest index**.
If no such node exists, return `-1`.

## Examples:
```
Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2

Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
```

# Sol 1: Two Pointers + Hash Set
## step-by-step approach:
1. Traverse from `node1` and record distances in `seen1`.
2. Traverse from `node2` and record distances in `seen2`.
3. For each node `i`, if reachable from both:
   * Compute `max(seen1[i], seen2[i])`.
   * Track the node with smallest such max distance (tie-break by index).
4. Return the best node found.

```python
def closestMeetingNode(e, n1, n2):
    seen1 = {}
    seen2 = {}
    d = 0
    while n1 != -1 and n1 not in seen1:
        seen1[n1] = d
        d += 1
        n1 = e[n1]
    
    d = 0
    while n2 != -1 and n2 not in seen2:
        seen2[n2] = d
        d += 1
        n2 = e[n2]

    res = -1
    min_dist = float('inf')
    for i in range(len(e)):
        if i in seen1 and i in seen2:
            max_d = max(seen1[i], seen2[i])
            if max_d < min_dist or (max_d == min_dist and i < res):
                res = i
                min_dist = max_d
    return res
```
Time: O(n)  
Space: O(n)  

# Sol 2: DFS Distance Map from Both Nodes
> Best for interviews

## step-by-step approach:
1. **Define `dist(start)`**: Traverses the graph from `start` and maps each reachable node to its distance using a loop (stops at -1 or cycle).
2. **Get distances**: Call `dist(n1)` → `d1`, and `dist(n2)` → `d2`.
3. **Compare common nodes**: For each node `i` in the graph, if it exists in both `d1` and `d2`, compute `max(d1[i], d2[i])`.
4. **Track minimum**: Keep the node with the smallest max distance (break ties by smallest index).
5. **Return result**: Return the best node found or -1 if none.

```python
def closestMeetingNode(e, n1, n2):
    def dist(start):
        d = {}
        s, l = start, 0
        while s != -1 and s not in d:
            d[s] = l
            s = e[s]
            l += 1
        return d

    d1, d2 = dist(n1), dist(n2)
    res, min_d = -1, float('inf')
    for i in range(len(e)):
        if i in d1 and i in d2:
            m = max(d1[i], d2[i])
            if m < min_d or (m == min_d and i < res):
                res, min_d = i, m
    return res
```
Time: O(n)  
Space: O(n)  

# Sol 3: BFS from Both Nodes
## step-by-step approach:
1. **bfs(s)**: Runs BFS from node `s`, returns distances array `d` where `d[i]` is distance from `s` to node `i`, or `-1` if unreachable.
2. Call `bfs(n1)` and `bfs(n2)` to get distance arrays `d1` and `d2`.
3. Iterate over all nodes:
   * If a node `i` is reachable from both `n1` and `n2`, compute `max(d1[i], d2[i])`.
   * Track the node with the smallest such max distance (tie-break by smaller index).
4. Return the chosen node.

```python
from collections import deque

def closestMeetingNode(e, n1, n2):
    def bfs(s):
        d = [-1] * len(e)
        q = deque([s])
        d[s] = 0
        while q:
            u = q.popleft()
            v = e[u]
            if v != -1 and d[v] == -1:
                d[v] = d[u] + 1
                q.append(v)
        return d

    d1, d2 = bfs(n1), bfs(n2)
    res, min_d = -1, float('inf')
    for i in range(len(e)):
        if d1[i] != -1 and d2[i] != -1:
            m = max(d1[i], d2[i])
            if m < min_d or (m == min_d and i < res):
                res, min_d = i, m
    return res
```
Time: O(n)  
Space: O(n)  

# Sol 4: One-pass while traversing both nodes simultaneously
## step-by-step approach:
1. Initialize two visited maps `v1` and `v2` for `n1` and `n2`.
2. Traverse from both nodes in parallel until paths end or nodes repeat (cycle).
3. Record each node and its distance from the respective source in `v1` and `v2`.
4. For each node in the graph:
   * If reachable from both, compute `max(v1[i], v2[i])`.
   * Track the node with the smallest such max distance (tie-break by index).
5. Return the best node.

```python
def closestMeetingNode(e, n1, n2):
    v1 = {}
    v2 = {}
    s1, s2 = n1, n2
    d1, d2 = 0, 0
    while s1 != -1 or s2 != -1:
        if s1 != -1:
            if s1 in v1: s1 = -1
            else:
                v1[s1] = d1
                s1 = e[s1]
                d1 += 1
        if s2 != -1:
            if s2 in v2: s2 = -1
            else:
                v2[s2] = d2
                s2 = e[s2]
                d2 += 1
    res, min_d = -1, float('inf')
    for i in range(len(e)):
        if i in v1 and i in v2:
            m = max(v1[i], v2[i])
            if m < min_d or (m == min_d and i < res):
                res, min_d = i, m
    return res
```
Time: O(n)  
Space: O(n)  

# Sol 5: Pre-initialize Distance Arrays and Traverse
## step-by-step approach:
1. Define `go()` to compute distances from a start node using a distance list `d`.
2. Traverse from `n1` and `n2` using `go()` to get distance arrays `d1` and `d2`.
3. For each node:

   * If reachable from both, calculate `max(d1[i], d2[i])`.
   * Track the node with the smallest such max distance (tie-break by index).
4. Return the best node index.

```python
def closestMeetingNode(e, n1, n2):
    def go(s):
        d = [-1] * len(e)
        l = 0
        while s != -1 and d[s] == -1:
            d[s] = l
            s = e[s]
            l += 1
        return d

    d1, d2 = go(n1), go(n2)
    res, min_d = -1, float('inf')
    for i in range(len(e)):
        if d1[i] != -1 and d2[i] != -1:
            m = max(d1[i], d2[i])
            if m < min_d or (m == min_d and i < res):
                res, min_d = i, m
    return res
```
Time: O(n)  
Space: O(n)  