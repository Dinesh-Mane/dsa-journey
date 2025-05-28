# [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/description/)

## Problem Statement
Given the head of a singly linked list, return the middle node of the linked list    
If there are two middle nodes, return the second middle node  

**Example**
```python
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3
```
```python
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one
```
## Possible Solutions – Brute Force to Optimized
## 1) Store All Nodes in List (for learning purposes) (Time: O(n), Space: O(n))  
Idea:
1. Store all nodes in an array/list  
2. Return node at index len(list)//2  

```python
arr = []
curr = head
while curr:
  arr.append(curr)
  curr = curr.next
return arr[len(arr)//2]
```

## 2) using Two Passes (Time: O(n), Space: O(1))  
Idea:
First traverse the entire list to count the total number of nodes, say `n`  
Then traverse again up to `n//2` and return that node 
```python
cnt = 0
curr = head
while curr:
  cnt+=1
  curr = curr.next
        
curr = head
for i in range(cnt//2):
  curr = curr.next
return curr
```

## 3) Optimized - Fast and Slow Pointer (O(n) time, O(1) space)  
Use two pointers:
- **Slow:** moves 1 step at a time  
- **Fast:** moves 2 steps at a time  

Because fast moves twice as fast, so when fast is done, slow is at the halfway point. 
```python
s=f=head
while f and f.next:
  s=s.next
  f=f.next.next
return s
```