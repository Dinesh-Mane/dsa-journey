# [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

## Problem Statement
Given the `head` of a linked list, return the node where the cycle begins.
If there is no cycle, return `None`.

> You must not modify the linked list. 

**Example**
```python
Input: head = [3,2,0,-4], pos = 1  
Output: Node with value 2
```
```python
Input: head = [1,2], pos = 0  
Output: Node with value 1
```
```python
Input: head = [1], pos = -1  
Output: None
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force – Track All Visited Nodes (Time: O(n), Space: O(n))  
Idea:
1. Keep a set() of visited nodes.    
2. If you ever visit the same node again, that’s the start of the cycle.  

```python
visited = set()
while head:
  if head in visited: return head  # first repeated node
  visited.add(head)
  head = head.next
return None
```
> Not space-efficient (O(n)), but simple to implement


## 2) Optimized – Floyd’s Cycle Detection (Tortoise and Hare Algorithm) (O(n) time, O(1) space)  
**Logic:** Once you detect a cycle using Floyd’s method, you can reset one pointer to head and move both 1 step at a time to find the start of cycle.

```python
slow = fast = head
while fast and fast.next:
  slow = slow.next
  fast = fast.next.next
  if slow == fast: break
else: return None
slow = head
while slow != fast:
  slow = slow.next
  fast = fast.next
return slow  # Start of cycle
```
`else:` can be directly used after a `while` or `for` loop.  
It runs only when the loop completes naturally, without hitting a `break`.  

## Bonus: Modify Node Structure (Use Extra Flag or Marker)
> Only for educational or custom node structure cases – Not allowed in LeetCode!

**Idea:** Modify each node to add a `visited` flag. If a node is visited again, it's part of the cycle.

**Why it doesn’t work on Leetcode:**
- Leetcode node structure is locked. You cannot modify the ListNode class.
- Violates: "Do not modify the linked list."

```python
class CustomListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    self.visited = False  # custom flag

def detectCycle(head):
  while head:
    if head.visited: return head
    head.visited = True
    head = head.next
return None
```