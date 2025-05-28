# [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/description/)

You need to implement a RecentCounter class that counts how many requests have been made within the last 3000 milliseconds. Each time the method ping(t) is called with a timestamp t (in milliseconds), it should record this request and return the number of requests that occurred in the time range [t - 3000, t]. The timestamps given are strictly increasing with each call.

# Solution 1: Simple List with Filtering (Brute Force)
**Idea Behind the Approach**  
Keep a list of all requests timestamps, and every time a new request `t` comes in, filter out the old requests that fall outside the 3000 ms window `[t - 3000, t]`.

### Step-by-step working:
1. Store all requests in a list self.requests:
    - On each call to `ping(t)`, append the new timestamp `t`.
2. Filter the list to keep only the requests in the time window `[t - 3000, t]`:
    - Use list comprehension to keep requests where `x >= t - 3000`.
3. Return the length of the filtered list:
    - This gives the count of recent requests within the last 3000 milliseconds.

```python
class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        # Filter requests that are in range [t-3000, t]
        self.requests = [x for x in self.requests if x >= t - 3000]
        return len(self.requests)
```
Time Complexity: O(n) per ping (due to filtering)  
Space Complexity: O(n)  

# Solution 2: Using Deque (Optimized Queue)
**Idea:** We want to count how many requests happened in the last 3000 milliseconds for each new request time `t`.

- We use a deque (double-ended queue) to efficiently keep track of the requests in the sliding time window `[t-3000, t]`.

### Step-by-step working:
1. Add the new request time `t` to the deque (at the right end):
    - This represents the newest request.

2. Remove all requests from the left of the deque that happened before `t - 3000`:
    - Because they are outside the 3000 milliseconds window and should no longer be counted.
    - This is done by checking the leftmost element (`self.q[0]`) and popping it if it's less than `t - 3000`.

3. Return the length of the deque:
    - After removing outdated requests, the deque only contains timestamps inside `[t - 3000, t]`.
    - So, its length is the count of recent calls.


```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
```
Time Complexity: Amortized O(1) per ping (each element pushed and popped once)  
Space Complexity: O(n)  

> Best for coding interviews

# Solution 3: Using Binary Search on Sorted List
```python
import bisect

class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        # Find left boundary index for t-3000 using binary search
        left_index = bisect.bisect_left(self.requests, t - 3000)
        return len(self.requests) - left_index
```
Time Complexity: O(log n) per ping due to binary search  
Space Complexity: O(n)   

# Solution 4: Using Balanced BST (e.g., SortedContainers SortedList)
```python
from sortedcontainers import SortedList

class RecentCounter:
    def __init__(self):
        self.requests = SortedList()

    def ping(self, t: int) -> int:
        self.requests.add(t)
        left_index = self.requests.bisect_left(t - 3000)
        return len(self.requests) - left_index
```
Time Complexity: O(log n) per ping for insert and bisect  
Space Complexity: O(n)   

---

## Summary:
| Solution                        | Time Complexity | Space Complexity |
| ------------------------------- | --------------- | ---------------- |
| 1. Simple List with Filtering   | O(n) per ping   | O(n)             |
| 2. Deque (Optimized Queue)      | Amortized O(1)  | O(n)             |
| 3. Binary Search on Sorted List | O(log n)        | O(n)             |
| 4. Balanced BST (SortedList)    | O(log n)        | O(n)             |
