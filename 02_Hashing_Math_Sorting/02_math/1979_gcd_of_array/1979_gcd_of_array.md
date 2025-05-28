# [1979. Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/?envType=problem-list-v2&envId=math)
An integer array `nums`. Return the greatest common divisor (GCD) of the smallest and largest number in the array.  
> Definition: The Greatest Common Divisor (GCD) of two numbers is the largest positive integer that evenly divides both numbers.

# Solution 1: Brute Force – Iterate from min(nums) down to 1
```python
def findGCD(nums):
    a, b = min(nums), max(nums)
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
```
Time Complexity: O(n) for min/max, O(min(nums)) for loop  
Space Complexity: O(1)  

# Solution 2: Built-in `math.gcd()`
```python
import math

def findGCD(nums):
    return math.gcd(min(nums), max(nums))
```
Time Complexity: O(n) for min/max, O(log(min, max)) for GCD  
Space Complexity: O(1)  

# Solution 3: Euclidean Algorithm (Custom GCD)
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def findGCD(nums):
    return gcd(min(nums), max(nums))
```
Time Complexity: O(n) for min/max, O(log(min, max)) for GCD  
Space Complexity: O(1)  

# Solution 4: Set Intersection
```python
def findGCD(nums):
    a, b = min(nums), max(nums)
    factors_a = {i for i in range(1, a+1) if a % i == 0}
    factors_b = {i for i in range(1, b+1) if b % i == 0}
    return max(factors_a & factors_b)
```
Time Complexity: O(n) for min/max, O(min(nums)) for factor sets  
Space Complexity: O(min(nums))  