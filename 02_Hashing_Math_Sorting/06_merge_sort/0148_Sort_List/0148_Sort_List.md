# [148. Sort List](https://leetcode.com/problems/sort-list/description/)
## Problem Statement
Given the head of a linked list, return the list after sorting it in ascending order.

## Examples:
```
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

# Sol 1. Convert to List → Sort → Convert Back
## step-by-step approach:

1. Extract all values from the linked list into an array `arr`.
2. Sort the array.
3. Create a new linked list from the sorted array.
4. Return the head of the new sorted list.


```python
def sortList(h):
    if not h: return None
    arr = []
    while h:
        arr.append(h.val)
        h = h.next
    arr.sort()
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next
```
OR  

1. Store all nodes (not just values) in list `a`.
2. Sort nodes based on their `val`.
3. Reconnect sorted nodes using `.next`.
4. Set the last node's `.next` to `None`.
5. Return new head (`a[0]`) or `None` if list is empty.

```python
def sortList(self, h):
    a = []
    while h: a.append(h), h = h.next
    a.sort(key=lambda x: x.val)
    for i in range(len(a)-1): a[i].next = a[i+1]
    if a: a[-1].next = None
    return a[0] if a else None
```
Time: O(n log n)  
Space: O(n)  

# Sol 2. Top-Down Merge Sort (Recursive)
> Best for interviews

### Merge Sort Summary:

1. **Divide** the list into two halves recursively until each part has one element.
2. **Sort** each half (this happens naturally via recursion).
3. **Merge** the sorted halves into a single sorted list.
4. Repeat merging upward until the whole list is sorted.

## step-by-step approach:
1. Base case: return if list is empty or has one node.
2. Use fast-slow pointer to split the list into two halves.
3. Recursively sort both halves.
4. Merge the two sorted halves.
5. Return the merged sorted list.

```python
def sortList(h):
    if not h or not h.next: return h

    def get_mid(head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def merge(l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next

    mid = get_mid(h)
    left = sortList(h)
    right = sortList(mid)
    return merge(left, right)
```
OR
```python
class Solution:
    def sortList(self, h):
        if not h or not h.next: return h
        s, f = h, h.next
        while f and f.next:
            s, f = s.next, f.next.next
        m, s.next = s.next, None
        l, r = self.sortList(h), self.sortList(m)
        d = tail = ListNode()
        while l and r:
            if l.val < r.val:
                tail.next, l = l, l.next
            else:
                tail.next, r = r, r.next
            tail = tail.next
        tail.next = l or r
        return d.next
```
Time: O(n log n)  
Space: O(log n) recursion stack  

# Sol 3. Bottom-Up Merge Sort (Iterative, O(1) Space)
## step-by-step approach:

1. **Get Size:** Count total nodes in the list.
2. **Iterative Merge:** Start with sublists of size 1, double the size in each pass.
3. **Split:** Break list into two parts of current step size.
4. **Merge:** Merge the two sorted parts, connect back to main list.
5. **Repeat:** Until entire list is merged in size ≥ full length.
6. **Return:** Head of the fully sorted list.

```python
def sortList(h):
    if not h or not h.next: return h

    def get_size(head):
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt

    def split(head, size):
        for i in range(size - 1):
            if head:
                head = head.next
            else:
                break
        rest = head.next if head else None
        if head:
            head.next = None
        return rest

    def merge(l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        while cur.next:
            cur = cur.next
        return dummy.next, cur

    size = get_size(h)
    dummy = ListNode(0)
    dummy.next = h
    step = 1

    while step < size:
        prev, curr = dummy, dummy.next
        while curr:
            left = curr
            right = split(left, step)
            curr = split(right, step)
            merged_head, merged_tail = merge(left, right)
            prev.next = merged_head
            prev = merged_tail
        step <<= 1
    return dummy.next
```
Time: O(n log n)  
Space: O(1)   

# Sol 4. Priority Queue (Min-Heap) Approach
## step-by-step approach:

1. **Push all nodes** into a min-heap based on their values (use index to break ties).
2. **Pop nodes** from heap one by one, reconnecting them in sorted order.
3. **Return** head of the newly sorted linked list.


```python
import heapq
class Solution:
    def sortList(self, h):
        if not h: return None
        a = []
        i = 0
        while h:
            heapq.heappush(a, (h.val, i, h))
            h = h.next
            i += 1
        d = c = ListNode(0)
        while a:
            _, _, n = heapq.heappop(a)
            n.next = None
            c.next = n
            c = c.next
        return d.next
```
Time: O(n log n)  
Space: O(n)  

---

| Approach                  | Time           | Space        | Interview Friendliness             |
| ------------------------- | -------------- | ------------ | ---------------------------------- |
| Convert to array + sort   | O(n log n)     | O(n)         | Simple but uses extra space        |
| **Top-Down Merge Sort**   | **O(n log n)** | **O(log n)** | **Best choice**                    |
| Bottom-Up Merge Sort (O1) | O(n log n)     | O(1)         | Harder to implement in interview   |
| Priority Queue (Heap)     | O(n log n)     | O(n)         | Not common for linked list sorting |

