# [2027) Minimum Moves to Convert String](https://leetcode.com/problems/minimum-moves-to-convert-string/description/?envType=problem-list-v2&envId=string)

## Problem Statement:
You are given a string `s` consisting of only `'X'` and `'O'`. You can convert any 3 consecutive characters to `'O'` in one move. The goal is to convert all `'X'` to `'O'` using the minimum number of moves.

# Solution 1: Replace Using Regex
Instead of simulating the transformation manually, we can count how many groups of 1 to 3 consecutive 'X' characters exist — because:
- A move always affects a block of 3, but
- Even a single 'X' still needs a full move (it will transform up to 3 characters anyway).

So:
- Each group of consecutive 'X's like 'XX' or 'XXX' or 'X' requires only one move.
- If we identify these non-overlapping 'X' clusters (of size 1 to 3), we can simply count them to get the answer.

```python
import re
def minimumMoves(s):
    return len(re.findall('X{1,3}', s))
```
Time Complexity: O(n)  
Space Complexity: O(n) (for regex match storage)  

# Solution 2: Greedy Skip Method
```python
def minimumMoves(s):
    i = 0
    moves = 0
    while i < len(s):
        if s[i] == 'X':
            moves += 1
            i += 3
        else:
            i += 1
    return moves
```
Time Complexity: O(n)  
Space Complexity: O(1)   

✅ This is the Optimal Solution.