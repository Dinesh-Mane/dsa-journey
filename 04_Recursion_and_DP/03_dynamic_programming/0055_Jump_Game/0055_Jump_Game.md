# [55. Jump Game](https://leetcode.com/problems/jump-game/description/)

## Problem Statement
You are given an array `nums` where each element represents your maximum jump length from that index. You start at index `0`, and you want to reach the last index.

Your task is to return `True` if it is possible to reach the last index, otherwise return `False`.

---

## Examples
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Input: nums = [0]
Output: True
Explanation: Already at the last index.
```
| Input         | Output  | Explanation                                        |
| ------------- | ------- | -------------------------------------------------- |
| `[2,3,1,1,4]` | `True`  | Jump from index 0 → 1 → 4 (end).                   |
| `[3,2,1,0,4]` | `False` | Stuck at index 3. Jump is `0`, can't proceed to 4. |
| `[0]`         | `True`  | Already at the last index.                         |


---

## Solution 1: Brute Force (Recursive Backtracking)

**Idea**: Try every possible jump from the current index recursively.

1. You try to jump to every possible next index from your current position.
2. At each position, you recursively explore all jumps from `pos` + 1 to `pos + nums[pos]`.
3. If any path leads you to or beyond the last index, you return `True`.
4. If no path leads you to the end, return `False`.

> `pos` = current index
```python
def canJump(nums):
    def backtrack(pos):
        if pos >= len(nums) - 1:
            return True
        furthest = min(pos + nums[pos], len(nums) - 1)
        for next_pos in range(pos + 1, furthest + 1):
            if backtrack(next_pos):
                return True
        return False
    return backtrack(0)
```

- **Time:** O(2^n) (TLE for large inputs)  
- **Space:** O(n) recursion stack  
- ❌ Too slow

**Dry Run:** `nums = [2,3,1,1,4]`
| Step | pos | next pos | Result        |
| ---- | --- | -------- | ------------- |
| 0    | 0   | 1, 2     | explores both |
| 1    | 1   | 2, 3, 4  | reaches 4 ✅   |

---

## Solution 2: Memoized DFS 

**Idea**: Same as DFS, but use memoization to avoid recomputation.

#### What is Memoized DFS?
It's a recursive approach (like brute-force DFS), but with memoization to avoid recalculating results for the same positions.
Memoization stores whether a particular index can lead to a successful path to the end.

#### Idea: For each index i:
- Try every possible jump from `i + 1` to `i + nums[i]`.
- If any of those jumps eventually reach the last index → return `True`
- Store this result in a `memo[i]` array so that future recursive calls can reuse it.
- If we already know the result from `i`, no need to recurse again.

```python
def canJump(nums):
    memo = [None] * len(nums)

    def dfs(i):
        if i >= len(nums) - 1:
            return True
        if memo[i] is not None:
            return memo[i]
        for j in range(1, nums[i] + 1):
            if dfs(i + j):
                memo[i] = True
                return True
        memo[i] = False
        return False

    return dfs(0)
```

- Time: O(n^2), Space: O(n)
- Better but not ideal

**Dry Run:** `nums = [3,2,1,0,4]`
| Step | Index | Memo State         |
| ---- | ----- | ------------------ |
| 0    | 0     | `[None,...]`       |
| 1    | 1     | `[None, None,...]` |
| ...  | 3     | Stuck              |

---

## Solution 3: BFS (Level by Level)
**Idea**: Treat the array as a graph and perform a breadth-first search.

```python
from collections import deque

def canJump(nums):
    queue = deque([0])
    visited = set([0])
    while queue:
        i = queue.popleft()
        for j in range(1, nums[i] + 1):
            next_i = i + j
            if next_i >= len(nums) - 1:
                return True
            if next_i not in visited:
                visited.add(next_i)
                queue.append(next_i)
    return len(nums) == 1
```

- Time: O(n^2), Space: O(n)
- Clear but heavy

**Dry Run:** `nums = [2,3,1,1,4]`
| Queue State | Current | Jump To | Result    |
| ----------- | ------- | ------- | --------- |
| `[0]`       | 0       | 1, 2    | Enqueue   |
| `[1,2]`     | 1       | 2,3,4   | Reaches ✅ |


---


## Solution 3: Dynamic Programming (Backward)
**Idea**: Start from the end and move backward. Mark positions from which you can reach the goal.

#### Idea Behind This Approach (Bottom-Up DP)
This approach builds the solution from the end of the array to the start.

- We create a DP array dp[i] which tells us: ✅ Can we reach the end from index i?
- **We know that:** `dp[-1] = True` because we’re already at the end if we are at the last index.
- Then we check from right to left:
  - Can we jump from index `i` to any future index `j` such that `dp[j] == True`?
  - If yes, we set `dp[i] = True`.

```python
def canJump(nums):
    n = len(nums)
    dp = [False] * n
    dp[-1] = True  # You can always reach the end from the end

    for i in range(n - 2, -1, -1):  # Start from second last index to front
        for j in range(1, nums[i] + 1):  # Try all possible jumps
            if i + j < n and dp[i + j]:  # If any future is reachable
                dp[i] = True
                break  # No need to check further jumps
    return dp[0]
```

- Time: O(n^2), Space: O(n)
- Clear but heavy

**Dry Run:** `nums = [2,3,1,1,4]`
| i   | dp                  |
| --- | ------------------- |
| 4   | `[_,_,_,_,True]`    |
| 3   | `[_,_,_,True,True]` |
| ... | ✅                   |

---

## Solution 5: Greedy (Backward)
**Idea**: Work backwards from the end and track the earliest index from which you can reach the end.

1. Start by assuming the last index is the “goal”.
2. Iterate from right to left.
3. If you are at index `i` and `i + nums[i] >= goal`, then you can jump to the goal from here, so update `goal = i`.
4. If after the loop `goal == 0`, it means you can reach the end from the start

```python
def canJump(nums):
    goal = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0
```

- Time: O(n), Space: O(1)
- Simple and efficient

**Dry Run:** `nums = [2,3,1,1,4]`
| i | goal |
| - | ---- |
| 3 | 4    |
| 1 | 1 ✅  |


---

## Solution 6: Greedy (Forward) – OPTIMAL
**Idea**: Iterate through the array and keep track of the maximum reachable index. If you ever get stuck, return `False`

We keep track of the farthest index we can reach (max_reach) as we move through the array:

- At each index `i`, check if `i` is within our max reach.
- If it is, update `max_reach` to be the farthest we can reach from here: `i + nums[i]`.
- If at any point `i > max_reach`, we can't reach this position — so return `False`
- If we finish the loop, return `True`

```python
def canJump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True
```

- Time: O(n), Space: O(1)
- Best choice

**Dry Run:** `nums = [3,2,1,0,4]`
| i | max\_reach                      |
| - | ------------------------------- |
| 0 | 3                               |
| 3 | 3                               |
| 4 | ❌ i > max\_reach → return False |


---

## Tips to Solve These Questions
| Tip                           | Reason                                                             |
| ----------------------------- | ------------------------------------------------------------------ |
| Think Greedy                  | You only care about the **furthest reach** at any step.            |
| Visualize jumps               | Imagine arrows pointing from current index to reachable positions. |
| Try Backward or Forward logic | If one is too complex, try the other direction.                    |
| Early exit saves time         | In greedy forward, break early if stuck.                           |

---

## ✅ Best for Interviews
**Solution 6 (Greedy Forward)** is:
- O(n) time
- Very intuitive after a few practices
- Constant space
- Easily extendable for follow-ups like min jumps

---
