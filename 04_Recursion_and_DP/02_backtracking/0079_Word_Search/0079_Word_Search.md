# [79. Word Search](https://leetcode.com/problems/word-search/description/)

## Problem Statement
Given an m x n grid of characters board and a string word, determine if the word exists in the grid

**Constraints:**
- The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically neighboring).
- The same letter cell may not be used more than once.

**Example**
```python
Input:
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
Output: True
```
```python
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```
```python
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

## Possible Solutions – Brute Force to Optimized
## 1) Brute Force DFS Without Backtracking
**Idea:** Start a DFS from every cell, exploring all paths without marking visited cells.  

**Time Complexity:** O((m×n) × 4^L), where L is the length of the word.  
**Space Complexity:** O(L) for the recursion stack.  

```python
def exist(board, word):
  rows, cols = len(board), len(board[0])

  def dfs(r, c, i):
    if i == len(word): return True
    if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]): return False

    # Explore all directions without marking visited
    return (dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1))

  for r in range(rows):
    for c in range(cols):
      if dfs(r, c, 0): return True
  return False
```
> Inefficient due to redundant computations.  
> Does not handle revisiting cells properly.  

## 2) DFS with Visited Matrix (O(n) Time, O(n) Space)
**Idea:** Use a separate visited matrix to track visited cells during DFS.   

**Time Complexity:** O((m×n) × 4^L)  
**Space Complexity:** O(m×n) for the visited matrix.  
```python
def exist(board, word):
  rows, cols = len(board), len(board[0])
  visited = [[False]*cols for _ in range(rows)]

  def dfs(r, c, i):
    if i == len(word): return True
    if (r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or board[r][c] != word[i]): return False

    visited[r][c] = True
    res = (dfs(r+1, c, i+1) or
          dfs(r-1, c, i+1) or
          dfs(r, c+1, i+1) or
          dfs(r, c-1, i+1))
    visited[r][c] = False
    return res

  for r in range(rows):
    for c in range(cols):
      if dfs(r, c, 0): return True
  return False
```
> Prevents revisiting the same cell in a path.  
> More accurate than the naive approach.  

## 3) DFS with In-Place Modification
**Idea:** Modify the board in-place to mark visited cells, restoring them after backtracking.

**Time Complexity:** O((m×n) × 4^L)  
**Space Complexity:** O(L) for the recursion stack.  
```python
def exist(board, word):
  rows, cols = len(board), len(board[0])

  def dfs(r, c, i):
    if i == len(word): return True
    if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]): return False

    temp = board[r][c]
    board[r][c] = '#'

    found = (dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1))

    board[r][c] = temp
    return found

  for r in range(rows):
    for c in range(cols):
      if dfs(r, c, 0): return True
  return False
```
> Avoids extra space for the visited matrix.  
> Efficient and commonly used in practice.  

## 4) DFS with Pruning
**Idea:** Before starting DFS, check if the board contains enough instances of each character in the word.

**Time Complexity:** Potentially reduced from O((m×n) × 4^L) due to early termination.  
**Space Complexity:** O(L) for the recursion stack.  
```python
from collections import Counter

def exist(board, word):
    rows, cols = len(board), len(board[0])
    board_count = Counter(char for row in board for char in row)
    word_count = Counter(word)
    for char in word_count:
        if word_count[char] > board_count.get(char, 0):
            return False

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]):
            return False

        temp = board[r][c]
        board[r][c] = '#'

        found = (dfs(r+1, c, i+1) or
                 dfs(r-1, c, i+1) or
                 dfs(r, c+1, i+1) or
                 dfs(r, c-1, i+1))

        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```
> Avoids unnecessary DFS calls when the word cannot be formed.  
> Improves efficiency in cases with insufficient characters.  

## 5) Optimized DFS with Early Termination
**Idea:** Combine in-place modification with early termination upon finding the word.

**Time Complexity:** Best case O(L), worst case O((m×n) × 4^L)  
**Space Complexity:** O(L) for the recursion stack.  

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]):
            return False

        temp = board[r][c]
        board[r][c] = '#'

        found = (dfs(r+1, c, i+1) or
                 dfs(r-1, c, i+1) or
                 dfs(r, c+1, i+1) or
                 dfs(r, c-1, i+1))

        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```
> Efficient in practice.  
> Terminates early when the word is found.  