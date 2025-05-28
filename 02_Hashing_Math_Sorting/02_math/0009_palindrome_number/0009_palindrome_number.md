# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/description/?envType=problem-list-v2&envId=math)

We are given an integer x. A number is a palindrome if it reads the same forward and backward.

Example:  
`121` → palindrome ✅  
`123` → not palindrome ❌  
`-121` → not palindrome ❌  


# Solution 1: String Reverse and Compare
```python
def isPalindrome(x):
    return str(x) == str(x)[::-1]
```
Time Complexity: O(n) where n is number of digits | Space Complexity: O(n) (due to string conversion and slicing)

# Solution 2: Manual Two-Pointer Check on String
```python
def isPalindrome(x):
    s = str(x)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]: return False
        left += 1
        right -= 1
    return True
```
Time Complexity: O(n) | Space Complexity: O(n) (due to string conversion)

# Solution 3: Reverse Integer Fully
```python
def isPalindrome(x):
    if x < 0: return False
    original = x
    rev = 0
    while x > 0:
        rev = rev * 10 + x % 10
        x //= 10
    return original == rev
```
Time Complexity: O(log₁₀x) | Space Complexity: O(1)

# Solution 4: Reverse Half of the Number (Optimized)

### Why This Approach?
This solution avoids converting the number to a string and instead reverses only half of the number to compare.  
**Why only half?**   
- For a number to be a palindrome, the first half must match the reversed second half.
- This avoids full reversal and unnecessary operations.

```python
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0): return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10
```
Time Complexity: O(log₁₀x) → best and most optimized  
Space Complexity: O(1)  
