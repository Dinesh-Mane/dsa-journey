# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

## Problem Statement
You are given a singly linked list where each node contains a binary digit (0 or 1). The linked list represents a binary number in order from the most significant bit (head) to the least significant bit (tail).  
Your task is to convert this binary number into its decimal (integer) equivalent.  

**Example**
```python
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
```
```python
Input: head = [0]
Output: 0
```
## Possible Solutions – Brute Force to Optimized
## 1) Convert to String and then to Integer (Simple but uses extra space) (Time: O(n), Space: O(n))
Idea: Traverse the linked list and append each node’s value to a string. Then use Python’s built-in `int()` function with base 2 to convert the binary string to an integer.
```python
s = ""
cur = head
while cur:
  s += str(cur.val)
  cur = cur.next
return int(s, 2)
```

## 2) Bit Manipulation (Optimal and Space Efficient) (O(n) time, O(1) space) 
**Idea:** Process the linked list node by node, updating the decimal number by shifting the current number left by 1 bit (equivalent to multiplying by 2) and adding the current node’s bit.  

**Example:**
Binary digits: 1 → 0 → 1
Steps:
- Start n = 0
- n = 0 * 2 + 1 = 1
- n = 1 * 2 + 0 = 2
- n = 2 * 2 + 1 = 5
```python
n = 0
cur = head
while cur:
  n = (n << 1) | cur.val
  cur = cur.next
return n
```
> `n << 1` म्हणजे n ला 2 ने multiply करणं (bitwise shift left).
> `| cur.val` म्हणजे त्या जागी नवीन bit set करणं (0 किंवा 1).
> List traverse करत decimal value update करत जातो.

