# [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

## Problem Statement
You are given the `head` of a singly linked list. Check whether there is a cycle in the linked list.  
A cycle means some node’s `next` points to an earlier `node` in the list.  

Return `True` if a cycle exists, otherwise `False`.

**Example**
```python
Input: head = [3,2,0,-4], pos = 1  # -4 → 2 (cycle)
Output: True
```
```python
Input: head = [1], pos = -1  # No cycle
Output: False
```
## Possible Solutions – Brute Force to Optimized
## 1) Use a list or set to store visited nodes (Time: O(n), Space: O(n))  
Idea:
1. While traversing the list, keep storing visited nodes in a set or list.  
2. If you see the same node again (i.e., its reference), a cycle exists.  

```python
visited = set()
while head:
  if head in visited: return True
  visited.add(head)
  head = head.next
return False
```
> Not space-efficient (O(n)), but simple to implement


## 2) Slight Optimization – Modify Node (Marking nodes) (Time: O(n), Space: O(1))  
**Idea: Only if modification is allowed**  
Mark each visited node by modifying it (like setting a dummy value or special marker).  
```python
while head:
  if head.val == float('inf'): return True
  head.val = float('inf')  # marking visited
  head = head.next
return False
```

## 3) Optimized – Floyd’s Cycle Detection (Tortoise and Hare Algorithm) (O(n) time, O(1) space)  
**Logic:**  
- Use two pointers:
  `slow` moves 1 step, `fast` moves 2 steps.
- If there is a cycle, they will eventually meet inside the loop.
- If there's no cycle, fast will reach the end (None).

Dry Run Idea:
```rust
1 -> 2 -> 3 -> 4 -> 5 -> 2 (cycle)
slow = 1 → 2 → 3 → 4  
fast = 1 → 3 → 5 → 3  
Eventually: slow == fast inside the loop
```
```python
slow = fast = head
while fast and fast.next:
  slow = slow.next
  fast = fast.next.next
  if slow == fast: return True
return False
```

## ## 3) Optimized – Floyd’s Cycle Detection (Tortoise and Hare Algorithm) (O(n) time, O(1) space)  
**Logic:** Once you detect a cycle using Floyd’s method, you can reset one pointer to head and move both 1 step at a time to find the start of cycle.

```python
slow = fast = head
while fast and fast.next:
  slow = slow.next
  fast = fast.next.next
  if slow == fast: break

slow = head
while slow != fast:
  slow = slow.next
  fast = fast.next
return slow  # Start of cycle
```