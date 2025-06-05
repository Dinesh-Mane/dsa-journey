# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
Given the `root` of a binary tree, return its maximum depth.  
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Examples
```
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2
```

---

# 1. Recursive DFS (Top-down)
## Step-by-Step Approach:
1. **First check if the current node is `None`**
   * If `r` is `None`, return `0`
     > This means we’ve reached beyond a leaf node (base case).

2. **Then recursively calculate depth of left and right subtrees**
   * `maxDepth(r.left)` → gives the depth of the left subtree.
   * `maxDepth(r.right)` → gives the depth of the right subtree.

3. **Add 1 to the maximum of the two depths**
   * `1 + max(...)` → adds current node level to the maximum subtree depth.

> This approach builds the final depth **bottom-up** by recursively evaluating all nodes and combining their results as we return from recursion.

```python
def maxDepth(r):
    if not r: return 0
    return 1 + max(maxDepth(r.left), maxDepth(r.right))
```
**Time:** O(n)  
**Space:** O(h)  

---

# 2. Recursive DFS (Bottom-up)
## Step-by-Step Approach:
1. **First define a helper DFS function with two parameters: node `n` and current depth `d`**
   * This allows us to **track the depth explicitly** as we traverse.

2. **Base Case: If `n` is None, return the current depth `d`**
   * This happens when we go beyond leaf nodes.
     > It gives the accumulated depth of that path.

3. **Then recursively call DFS for left and right child nodes with `d+1`**
   * `dfs(n.left, d+1)` → goes down the left subtree and increases depth.
   * `dfs(n.right, d+1)` → does the same for the right subtree.

4. **Return the maximum of both subtree depths**
   * `max(...)` ensures we get the **longest path** from root to leaf.

> This approach uses a **top-down DFS traversal** with explicit depth tracking.

```python
def maxDepth(r):
    def dfs(n, d):
        if not n: return d
        return max(dfs(n.left, d+1), dfs(n.right, d+1))
    return dfs(r, 0)
```
**Time:** O(n)  
**Space:** O(h)  

---

# 3. Iterative DFS using Stack
## Step-by-Step Approach:
1. **First check if the root node `r` is None**
   * If yes, return `0` as the tree is empty.

2. **Initialize a stack `stk` with a tuple `(r, 1)`**
   * This holds the root node and its depth `1`.
   * Also initialize `d = 0` to track maximum depth found so far.

3. **While the stack is not empty, do the following:**
   * Pop the top element to get current node `n` and its depth `h`.
   * If the node exists:
     * Update max depth: `d = max(d, h)` → keeps track of the deepest level seen.
     * Push left child with depth `h+1` → `stk.append((n.left, h+1))`
     * Push right child with depth `h+1` → `stk.append((n.right, h+1))`

4. **Return `d`**
   * It contains the **maximum depth** reached by any path from root to leaf.

> This is a **depth-first traversal using an explicit stack**, where we track the height at each node iteratively.

```python
def maxDepth(r):
    if not r: return 0
    stk, d = [(r, 1)], 0
    while stk:
        n, h = stk.pop()
        if n:
            d = max(d, h)
            stk.append((n.left, h+1))
            stk.append((n.right, h+1))
    return d
```

**Time:** O(n)
**Space:** O(h)

---

# 4. Iterative BFS using Queue
## Step-by-Step Approach:
1. **First check if the root node `r` is None**
   * If yes, return `0` since the tree is empty.

2. **Initialize a queue `q` with the root node `r`**
   * Also initialize `d = 0` to count the levels (i.e., depth).

3. **While the queue is not empty, repeat the following:**
   * For each node at the current level (`for _ in range(len(q))`):
     * Pop the node from the front: `n = q.popleft()`
     * If `n.left` exists, append it to the queue.
     * If `n.right` exists, append it to the queue.
   * After processing all nodes at this level, increment depth: `d += 1`

4. **Return `d`**
   * It now holds the total number of levels in the binary tree.

> This is a **breadth-first search (BFS)** approach using a queue to process nodes **level by level**, and incrementing the depth at the end of each level.

```python
from collections import deque
def maxDepth(r):
    if not r: return 0
    q, d = deque([r]), 0
    while q:
        for _ in range(len(q)):
            n = q.popleft()
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        d += 1
    return d
```
**Time:** O(n)  
**Space:** O(w)  

---

# 5. Using `deque` with tuple depth tracking
## Step-by-Step Approach:
1. **First check if the root node `r` is None**
   * If yes, return `0` since the tree has no depth.

2. **Initialize a queue `q` with a tuple of root node and its level 1**
   * Also initialize `d = 0` to keep track of max depth.

3. **While the queue is not empty, repeat the following:**
   * Pop the front element: `n, h = q.popleft()`
     * `n` is the current node
     * `h` is the current depth level
   * Update `d = max(d, h)` to track the deepest level seen so far
   * If `n.left` exists, enqueue `(n.left, h+1)`
   * If `n.right` exists, enqueue `(n.right, h+1)`

4. **Return `d`**
   * It now holds the maximum depth of the binary tree.

> This approach uses **Breadth-First Search (BFS)** with **depth tracking via queue tuples**, ensuring you always have the current depth level alongside each node during traversal.

```python
from collections import deque
def maxDepth(r):
    if not r: return 0
    q, d = deque([(r,1)]), 0
    while q:
        n, h = q.popleft()
        d = max(d, h)
        if n.left: q.append((n.left, h+1))
        if n.right: q.append((n.right, h+1))
    return d
```

**Time:** O(n)  
**Space:** O(w)  

---

# 6. Using Level Counter BFS
## Step-by-Step Approach:
1. **First check if the root node `r` is None**
   * If yes, return `0` since the tree is empty.

2. **Initialize a list `cur` with the root node**
   * This list represents the current level of nodes to process.
   * Also initialize `d = 0` to track depth.

3. **While `cur` is not empty, do the following:**
   * Initialize `nxt = []` to store nodes for the next level.
   * For each node `n` in `cur`:
     * If `n.left` exists, add it to `nxt`
     * If `n.right` exists, add it to `nxt`
   * Set `cur = nxt` to move to the next level.
   * Increment `d` by 1 after finishing the current level.

4. **Return `d`**
   * This is the number of levels traversed, i.e., the maximum depth.

> This is a **level-order traversal (BFS)** using plain lists instead of a queue, tracking depth by processing each level in sequence.

```python
def maxDepth(r):
    if not r: return 0
    cur = [r]
    d = 0
    while cur:
        nxt = []
        for n in cur:
            if n.left: nxt.append(n.left)
            if n.right: nxt.append(n.right)
        cur = nxt
        d += 1
    return d
```
**Time:** O(n)  
**Space:** O(w)  

---

# 7. BFS with `queue.Queue`
## Step-by-Step Approach:
1. **Check if root `r` is None**
   * If yes, return `0` since the tree has no depth.

2. **Initialize a `Queue` and add root node `r`**
   * Also set `d = 0` to track the depth level.

3. **While the queue is not empty:**
   * Use `q.qsize()` to determine the number of nodes at the current level.
   * For each of these nodes:
     * `q.get()` removes the node.
     * If `n.left` exists, enqueue it.
     * If `n.right` exists, enqueue it.
   * After processing the level, increment `d` by 1.

4. **Return `d`**
   * This gives the maximum depth of the tree.

> This is a **level-order BFS approach using `queue.Queue`**, which ensures thread-safe FIFO queue handling (mostly relevant in multi-threaded apps).

```python
from queue import Queue
def maxDepth(r):
    if not r: return 0
    q, d = Queue(), 0
    q.put(r)
    while not q.empty():
        for _ in range(q.qsize()):
            n = q.get()
            if n.left: q.put(n.left)
            if n.right: q.put(n.right)
        d += 1
    return d
```
**Time:** O(n)  
**Space:** O(w)  

---

# 8. Functional Recursive One-liner
## Step-by-Step approach:
1. **Check if root `r` is None**
   * If yes, return `0`.

2. **If `r` exists**, recursively compute the max depth of left and right subtrees using `map(maxDepth, (r.left, r.right))`.
   * This applies `maxDepth` to both children in one concise call.

3. **Add 1** to the maximum of the two depths to include the current node level.
4. **Return the result** as the maximum depth of the tree rooted at `r`.

> This is a concise recursive one-liner using `map` and `max` to traverse the tree.

```python
def maxDepth(r): return 1 + max(map(maxDepth, (r.left, r.right))) if r else 0
```
**Time:** O(n)  
**Space:** O(h)  

---

# Summary Table

| Solution                           | Time | Space | Type / Style           | Interview Friendly |
| ---------------------------------- | ---- | ----- | ---------------------- | ------------------ |
| **Recursive DFS (Top-down)**       | O(n) | O(h)  | Classic recursion      | ✅ **Best**         |
| Recursive DFS (Bottom-up)          | O(n) | O(h)  | Depth passed in args   | Good               |
| Iterative DFS (Stack)              | O(n) | O(h)  | Simulates recursion    | Good               |
| Iterative BFS (Queue - level wise) | O(n) | O(w)  | Standard BFS           | ✅ Very Good        |
| BFS with (node, depth) tuples      | O(n) | O(w)  | Depth tracked manually | Good               |
| BFS using two lists (cur/nxt)      | O(n) | O(w)  | Level counter pattern  | OK                 |
| BFS with `queue.Queue`             | O(n) | O(w)  | Alternative lib usage  | OK                 |
| Functional Recursion One-liner     | O(n) | O(h)  | Compact, not readable  | ❌ Not Recommended  |

---
