# [1290. Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/)

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
## 1: Convert to String and then to Integer (Simple but uses extra space) (Time: O(n), Space: O(n))
Idea: Traverse the linked list and append each node’s value to a string. Then use Python’s built-in `int()` function with base 2 to convert the binary string to an integer.
```python
s = ""
cur = head
while cur:
  s += str(cur.val)
  cur = cur.next
return int(s, 2)
```

## 2: Bit Manipulation (Optimal and Space Efficient) (O(n) time, O(1) space) 
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
> best for interviews
> `n << 1` म्हणजे n ला 2 ने multiply करणं (bitwise shift left).
> `| cur.val` म्हणजे त्या जागी नवीन bit set करणं (0 किंवा 1).
> List traverse करत decimal value update करत जातो.

## 3: List to String
#### Step-by-Step Breakdown:
1. Create a list `a`:
    - We'll store the binary digits (`0` or `1`) of the linked list in a list as strings.
2. Traverse the linked list:
    - At each node, convert the value (`0` or `1`) to a string and append it to list `a`.
3. After traversal:
    - Example list: `a = ['1', '0', '1']`
4. Join the list into a single string:
    - `'101' = ''.join(a)`
5. Convert binary string to decimal:
    - `int('101', 2)` → 5
6. Return the result.

```python
a = []
while head:
  a.append(str(head.val))
  head = head.next
return int(''.join(a), 2)
```
Time: O(n), Space: O(n)


## 4: Recursion
This is a recursive post-order traversal approach where we calculate the decimal value from right to left (from least significant bit to most significant).
```python
def dfs(node):
  if not node: return 0, 0
  v, p = dfs(node.next)
  return (node.val << p) + v, p + 1
return dfs(head)[0]
```
Time: O(n), Space: O(n)