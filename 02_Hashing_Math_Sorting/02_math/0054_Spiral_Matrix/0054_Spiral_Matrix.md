# [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/description/)

## Problem Statement
Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.  
**Example**
```python
Input: matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```
```python
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```
## Possible Solutions – Brute Force to Optimized
## 1) Most Optimized – Layer-by-Layer Traversal (Using boundaries) (Time: O(m * n), Space: O(1))  
Idea: We define 4 boundaries:  
> top → सुरुवातीला 0  
> bottom → m - 1  
> left → 0  
> right → n - 1  

We then move in 4 directions:
> Left to Right → on top row  
> Top to Bottom → on right column  
> Right to Left → on bottom row  
> Bottom to Top → on left column

Each time, we shrink the boundary.
```python
res = []
if not matrix: return res
top, bottom = 0, len(matrix) - 1
left, right = 0, len(matrix[0]) - 1
while top <= bottom and left <= right:
  for i in range(left, right + 1): res.append(matrix[top][i])
  top += 1
  for i in range(top, bottom + 1): res.append(matrix[i][right])
  right -= 1
  if top <= bottom:
    for i in range(right, left - 1, -1): res.append(matrix[bottom][i])
    bottom -= 1
  if left <= right:
    for i in range(bottom, top - 1, -1): res.append(matrix[i][left])
    left += 1
return res
```
## 2) Simulated Direction Movement with Visited Matrix (O(m * n) time, O(m * n) space)  
Idea:
> Use a visited matrix to mark visited cells.
> Use direction vectors:

```python
Right  → (0, 1)
Down   → (1, 0)
Left   → (0, -1)
Up     → (-1, 0)
```
When hitting a boundary or visited cell, change direction.

```python
if not matrix:return []
m, n = len(matrix), len(matrix[0])
visited = [[False]*n for _ in range(m)]
res = []

dir = [(0,1), (1,0), (0,-1), (-1,0)]   # directions: right, down, left, up
row = col = dir_index = 0

for _ in range(m * n):
  res.append(matrix[row][col])
  visited[row][col] = True

  next_row = row + dir[dir_index][0]   # Next cell
  next_col = col + dir[dir_index][1]

  # Check if we need to change direction
  if (0 <= next_row < m and 0 <= next_col < n and not visited[next_row][next_col]):  
    row, col = next_row, next_col
  else:
    # Change direction
    dir_index = (dir_index + 1) % 4
    row += dir[dir_index][0]
    col += dir[dir_index][1]
return res
```
## 3) Mathematical Approach (Using a layer-by-layer method) (O(m * n) time, O(m * n) space)  
This approach considers each "layer" of the matrix, making it a bit more efficient by directly working with the matrix indices rather than modifying the matrix structure during traversal.  

```python
result = []
while matrix:
  result.extend(matrix.pop(0))  # Top row
  if matrix and matrix[0]:
    for row in matrix: result.append(row.pop())  # Right column
  if matrix: result.extend(matrix.pop()[::-1])  # Bottom row (reversed)
  if matrix and matrix[0]:
    for row in matrix[::-1]: result.append(row.pop(0))  # Left column
return result
```

## 4) Optimized - Pop and Manipulate Matrix Structure (No need for boundaries) (O(m * n) time, O(m * n) space)  
This approach optimizes the code by eliminating explicit boundary checks and only focusing on looping through rows and columns directly.  

```python
result = []
while matrix:
  result += matrix.pop(0)  # Get the first row
  if matrix and matrix[0]:
    for row in matrix: result.append(row.pop())     # Get the last element of each row
  if matrix: result += matrix.pop()[::-1]      # Get the last row in reverse order
  if matrix and matrix[0]:
    for row in matrix[::-1]: result.append(row.pop(0))    # Get the first element of each row
return result
```