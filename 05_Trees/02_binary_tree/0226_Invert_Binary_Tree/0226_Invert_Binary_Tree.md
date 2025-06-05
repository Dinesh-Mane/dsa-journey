# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)
Given the root of a binary tree, invert the tree, and return its root.

### Example 1
Input: root = [4,2,7,1,3,6,9]  
Output: [4,7,2,9,6,3,1]

![](./invert.jpg)

### Example 2
Input: root = [2,1,3]  
Output: [2,3,1]

![](./invert2.jpg)

---

# 1. **Recursive DFS**
## Step-by-Step Approach:
1. **First, check if the node is not null (`if r:`)**
   – This ensures that we only process existing nodes.
   – If the node is `None`, recursion stops, and the function returns `None`.

2. **Then recursively call `inv(r.right)` and `inv(r.left)`**
   – This goes **down to the leaves** of the binary tree, swapping from bottom-up.

3. **Swap the left and right children using `r.left, r.right = inv(r.right), inv(r.left)`**
   – This inverts the current node by assigning the result of the recursive calls in reversed order.

4. **Finally, return the current node `r`**
   – This passes the updated/inverted subtree back up the recursion chain.

```python
def inv(r):
    if r:
        r.left, r.right = inv(r.right), inv(r.left)
    return r
```
**Time:** O(n), **Space:** O(h)

---

# 2. **Iterative DFS with Stack**
## Step-by-Step Approach:
1. **First, check if the root is null (`if not r: return`)**
   – This avoids processing when the tree is empty.

2. **Initialize a stack with the root node (`stk = [r]`)**
   – This sets up iterative DFS using a stack.

3. **While the stack is not empty, pop a node `n = stk.pop()`**
   – Visits nodes in depth-first order.

4. **Swap its children using `n.left, n.right = n.right, n.left`**
   – Inverts the current node by swapping left and right.

5. **Push the non-null children to the stack (`stk.append(...)`)**
   – Ensures all nodes in the tree are processed.

6. **Finally, return the root node `r`**
   – Returns the inverted binary tree.

```python
def inv(r):
    if not r: return
    stk = [r]
    while stk:
        n = stk.pop()
        n.left, n.right = n.right, n.left
        if n.left: stk.append(n.left)
        if n.right: stk.append(n.right)
    return r
```
**Time:** O(n), **Space:** O(n)

---

# 3. **Iterative BFS with Queue**
## Step-by-Step Approach:
1. **First, check if the root is null (`if not r: return`)**
   – Skips processing if the tree is empty.

2. **Initialize a queue with the root node (`q = deque([r])`)**
   – Sets up BFS using a queue for level-order traversal.

3. **While the queue is not empty, pop a node (`n = q.popleft()`)**
   – Processes nodes level by level.

4. **Swap its children using `n.left, n.right = n.right, n.left`**
   – Inverts the current node.

5. **If children are not null, enqueue them (`q.append(...)`)**
   – Ensures all nodes are visited and inverted.

6. **Finally, return the root node `r`**
   – Returns the root of the inverted binary tree.

```python
from collections import deque
def inv(r):
    if not r: return
    q = deque([r])
    while q:
        n = q.popleft()
        n.left, n.right = n.right, n.left
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    return r
```
**Time:** O(n), **Space:** O(n)

---

# 4. **Functional Style with Lambda + Recursion**
## Step-by-Step Approach:
1. **Check if node is non-null (`r and ...`)**
   – Ensures we only process actual nodes.

2. **Recursively invert right and left subtrees (`inv(r.right), inv(r.left)`)**
   – Goes to the leaves first, inverting bottom-up.

3. **Swap using assignment expression (`r.left, r.right := ...`)**
   – Uses the walrus operator `:=` for inline assignment (Python 3.8+).

4. **Return the current node `r`**
   – Final result is the inverted subtree rooted at `r`.

```python
inv = lambda r: r and (r.left, r.right := inv(r.right), inv(r.left)) and r
```
**Time:** O(n), **Space:** O(h)

---

# 5. **Recursive Post-order Style**
## Step-by-Step Approach:
1. **Check if node is `None` (`if not r: return`)**
   – Base case to stop recursion for leaf children.

2. **Recursively invert left and right subtrees (`inv(r.left)`, `inv(r.right)`)**
   – Get inverted versions of left (`l`) and right (`r_`) subtrees.

3. **Swap the inverted subtrees (`r.left, r.right = r_, l`)**
   – Assign right subtree to `left` and left subtree to `right`.

4. **Return the current node `r`**
   – Returns the root of the inverted subtree.

```python
def inv(r):
    if not r: return
    l = inv(r.left)
    r_ = inv(r.right)
    r.left, r.right = r_, l
    return r
```
**Time:** O(n), **Space:** O(h)

---

# 6. **Recursive Pre-order Style**
## Step-by-Step Approach:
1. **Check if node is `None` (`if not r: return`)**
   – This stops the recursion once a leaf node is reached.

2. **Swap left and right children (`r.left, r.right = r.right, r.left`)**
   – Inverts the current node immediately.

3. **Recursively call `inv` on left and right children (`inv(r.left)`, `inv(r.right)`)**
   – Continues inversion down the tree after the current swap.

4. **Return the node `r`**
   – Returns the root of the fully inverted subtree.

```python
def inv(r):
    if not r: return
    r.left, r.right = r.right, r.left
    inv(r.left)
    inv(r.right)
    return r
```
**Time:** O(n), **Space:** O(h)

---

# 7. **One-Liner with Map (DFS)**
## Step-by-Step Approach:
1. **Check if node is not `None` (`r and ...`)**
   – Stops recursion if node is `None`.

2. **Recursively invert right subtree and set it as left child (`setattr(r, 'left', inv(r.right))`)**
   – Inverts right subtree and assigns it to left.

3. **Recursively invert left subtree and set it as right child (`setattr(r, 'right', inv(r.left))`)**
   – Inverts left subtree and assigns it to right.

4. **Return the node `r`**
   – Returns the root of the inverted subtree.

```python
def inv(r): return r and (setattr(r, 'left', inv(r.right)), setattr(r, 'right', inv(r.left))) and r
```
**Time:** O(n), **Space:** O(h)

---

# 8. **Iterative with List as Queue**
## Step-by-Step Approach:
1. **Check if the root node is `None` (`if not r: return`)**
   – Stops if tree is empty.

2. **Initialize a queue/list with the root node (`q = [r]`)**
   – Used for level order traversal.

3. **While queue is not empty, pop the first node (`n = q.pop(0)`)**
   – Process nodes in FIFO order (BFS).

4. **Swap left and right children (`n.left, n.right = n.right, n.left`)**
   – Inverts the current node.

5. **Append left and right children to queue if they exist (`if n.left: q.append(n.left)`, etc.)**
   – Continue traversal on children.

6. **Return the root node `r`**
   – The inverted tree root.

```python
def inv(r):
    if not r: return
    q = [r]
    while q:
        n = q.pop(0)
        n.left, n.right = n.right, n.left
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    return r
```
**Time:** O(n²), **Space:** O(n) — due to `.pop(0)`

---

## Summary Table

| Solution # | Description                | Time  | Space | Type                  |
| ---------- | -------------------------- | ----- | ----- | --------------------- |
| 1          | Recursive DFS (clean)      | O(n)  | O(h)  | ✅ Best for interviews |
| 2          | Iterative DFS (stack)      | O(n)  | O(n)  | Stack-based           |
| 3          | Iterative BFS (queue)      | O(n)  | O(n)  | Level-order           |
| 4          | Lambda recursive (compact) | O(n)  | O(h)  | Pythonic trick        |
| 5          | Recursive post-order       | O(n)  | O(h)  | Classic               |
| 6          | Recursive pre-order        | O(n)  | O(h)  | ✅ Classic & readable  |
| 7          | One-liner with `setattr`   | O(n)  | O(h)  | Hacky trick           |
| 8          | List-based BFS (slow)      | O(n²) | O(n)  | Not preferred         |

---
