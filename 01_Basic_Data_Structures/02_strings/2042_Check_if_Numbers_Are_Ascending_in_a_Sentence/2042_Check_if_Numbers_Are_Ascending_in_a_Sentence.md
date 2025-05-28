# [2042. Check if Numbers Are Ascending in a Sentence](https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/?envType=problem-list-v2&envId=string)
We are given a sentence that contains words and positive numbers, separated by spaces.  
We need to check if all the numbers in the sentence are strictly increasing (each number is greater than the one before it).

# Solution 1: Using regex to extract numbers
**Idea Behind the Approach**  
We don’t care about the words — only the numbers in the sentence.  
So, the plan is:  
1. Extract all numbers from the sentence.
2. Convert them to integers.
3. Check whether the list of numbers is strictly increasing.

```python
import re
def areNumbersAscending(s):
    nums = list(map(int, re.findall(r'\d+', s)))
    return all(nums[i] < nums[i+1] for i in range(len(nums) - 1))
```
`re.findall(r'\d+', s)` uses a regex to find all continuous digit sequences in the string.  
`\d+` means: one or more digits  

Example:
```python
s = "a puppy has 2 eyes and 4 legs"
re.findall(r'\d+', s)  →  ['2', '4']
```
Time Complexity: O(n) — where n is the length of the string  
Space Complexity: O(k) — for k numbers in the sentence    

# Solution 2: Split and check numeric tokens
```python
def areNumbersAscending(s):
  s = s.split()
  prev = -1
  for i in s:
    if i.isdigit():
      if int(i)<=prev: return False
    prev = int(i)
  return True
```
Time Complexity: O(n) — single pass over string, then checking tokens  
Space Complexity: O(1) — no extra space except a few variables  

# Solution 3: Generator with zip (Compact Pythonic)
```python
import re
def areNumbersAscending(s):
    nums = list(map(int, re.findall(r'\d+', s)))
    return all(x < y for x, y in zip(nums, nums[1:]))
```
Time Complexity: O(n)  
Space Complexity: O(k)  

# Solution 4: On-the-fly parse without storing all numbers
```python
def areNumbersAscending(s):
    i = 0
    prev = -1
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            if num <= prev:
                return False
            prev = num
        else:
            i += 1
    return True
```
Time Complexity: O(n)  
Space Complexity: O(1)  

> This is the most optimized solution (O(n) time and O(1) space), with no regex, no split, no list storage — best for interviews and large strings.