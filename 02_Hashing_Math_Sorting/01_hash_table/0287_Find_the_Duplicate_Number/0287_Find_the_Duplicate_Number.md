# [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/)

## Problem Statement
एक integer array nums दिला आहे ज्यामध्ये n + 1 elements आहेत आणि प्रत्येक element 1 ते n च्या दरम्यानचं आहे. ह्या array मध्ये exactly एकच number duplicate आहे, पण तो एकाहून अधिक वेळा येऊ शकतो.

📌 म्हणून तुला duplicate number find करायचा आहे, पण लक्षात ठेव:
> Array modify करू नये (म्हणजे inplace sort, etc. नाही)  
> Extra space O(1) च वापरायचा आहे (no hashmaps, etc.)

**Example**
```python
Input: nums = [1, 3, 4, 2, 2]
Output: 2
```
```python
Input: nums = [3, 1, 3, 4, 2]
Output: 3
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Check every pair (O(n²) time, O(1) space)
```python
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]: return nums[i]
```
## 2) Using Sorting (O(n log n) time but violates space constraint) 
**Idea:** Array sort करा. आणि consecutive elements compare करत जा. जर दोन element सारखे असले, तर तोच duplicate.  
```python
nums.sort()  #In-place sort -> space -> O(1) (if in-place sort is allowed)
for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]: return nums[i]
```
```python
nums = sorted(nums)  #creates new copy, not in-place -> space -> O(n)
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]: return nums[i]
```
## 3) Using HashSet (O(n) Time, O(n) Space)
**Logic:** सर्व numbers एका set मध्ये घाला. जर number आधीच असला तर तो duplicate आहे.
```python
hashh = set() #set() madhe lookup O(1) madhe hoto tyamule time khup vachato
for n in nums:
    if n in hashh: return n
    hashh.add(n)
```
## 4) Binary Search on Value Range (O(n log n) time, O(1) space)
**ही पद्धत array वर binary search नाही करते, तर ती values च्या range वर करते.**  
> **Logic:**  
> low = 1 आणि high = n (value range)  
> प्रत्येक वेळी mid = (low + high) // 2 काढा  
> मग array मध्ये count करा की किती numbers आहेत जे ≤ mid आहेत  
> If count > mid → duplicate exists in lower half || Else → duplicate is in upper half  
> Loop चालवत राहा जोपर्यंत low < high  

```
Input: nums = [1, 3, 4, 2, 2]
n = 4, low = 1, high = 4

Iteration 1:
    mid = (1+4)//2 = 2
    count of nums ≤ 2 = 3 (values: 1, 2, 2)
    count > mid → duplicate is in [1, 2] → high = mid

Iteration 2:
    mid = (1+2)//2 = 1
    count of nums ≤ 1 = 1
    count == mid → duplicate in [2,2] → low = mid+1

low == high == 2 → duplicate is 2 ✅
```
```python
low = 1
high = len(nums) - 1  # because nums has n+1 elements

while low < high:
    mid = (low + high) // 2
    cnt = sum(n <= mid for n in nums) #array मधून सगळी values scan करते आणि mid पेक्षा <= किती elements आहेत ते मोजते.
    if count > mid: high = mid
    else: low = mid + 1
return low
```
## 5) Optimized - Floyd’s Cycle Detection (O(n) time, O(1) space)
> **Idea Behind This Approach:**    
> हा problem "Linked List Cycle Detection" ह्या algorithm वर आधारित आहे.  
> हे तुमचं array एक प्रकारे linked list बनवतंय:  
> nums[i] म्हणजे "next pointer"  
> म्हणजे, जर nums = [1,3,4,2,2] असेल, तर i = 0 पासून आपण nums[0] = 1, मग nums[1] = 3 असे "jump" करतो.  
> ✅ एकदा duplicate number असेल तर त्यातून cycle तयार होतो – आणि आपण Floyd's Algorithm ने तो detect करू शकतो.

**Dry Run: nums = [1, 3, 4, 2, 2]**
```
Step 1: Slow = nums[0] = 1
        Fast = nums[nums[0]] = nums[1] = 3

Step 2: Slow = nums[1] = 3
        Fast = nums[nums[3]] = nums[2] = 4

Step 3: Slow = nums[3] = 2
        Fast = nums[nums[4]] = nums[2] = 4

Step 4: Slow = nums[2] = 4
        Fast = nums[nums[2]] = nums[4] = 2

Step 5: Slow = nums[4] = 2
        Fast = nums[nums[4]] = nums[2] = 4

(They will meet at the same point after some steps)

Once they meet, keep one pointer at start and another at meet point, move both by 1 step until they meet again → that is duplicate.
```
```python
slow = nums[0]
fast = nums[0]

# Phase 1: Detect cycle
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast: break

# Phase 2: Find entry point
slow = nums[0]
while slow != fast:
    slow = nums[slow]
    fast = nums[fast]

return slow
```