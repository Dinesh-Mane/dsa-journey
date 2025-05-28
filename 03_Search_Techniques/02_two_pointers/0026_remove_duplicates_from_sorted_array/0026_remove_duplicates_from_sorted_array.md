# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

## Problem Statement
एक sorted array `nums` दिला आहे. त्यातून duplicate elements काढून टाकायचे आहेत – म्हणजे प्रत्येक number array मध्ये एकदाच यायला पाहिजे.  
Return करायचंय unique elements ची संख्या.  
> हे सगळं inplace करायचं आहे, म्हणजे नवीन array वापरायचा नाही आणि space O(1) वापरायचा आहे.

**Example**
```python
Input: nums = [1,1,2]
Output: 2  
Explanation: Array becomes [1,2,_], where _ is garbage (ignored).
```
```python
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5  
Explanation: Array becomes [0,1,2,3,4,...]
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Using Extra Array (❌ Violates space constraint)  
Idea: एका नवीन array मध्ये unique values टाका. पण ही पद्धत extra space वापरते (O(n)), म्हणून constraint नुसार allow नाही.
```python
res = []
for n in nums:
    if not res or res[-1] != n:  #jr res array empty asel kiva tyachya shevtcha element ha n nasel
        res.append(n)
return len(res)
#Wrong Answer : karan original array madhe sort karun uniquw number starting la anayche hote
```
jr nusta list of unique elements magitla asta tr asa kela asta: 
```python
return list(set(nums))
```
jr sorted list of unique elements magitla asta tr asa kela asta: 
```python
return sorted(set(nums))
```
jr nusta unique nubers cha count magitla asta tr asa kela asta: 
```python
return len(set(nums))
``` 
## 2) Using `set()` and sort  (O(n log n) time, O(n) space) 
**Idea:** Array sort करा. आणि consecutive elements compare करत जा. जर दोन element सारखे असले, तर तोच duplicate.  
```python
unique = sorted(set(nums))
for i in range(len(unique)):  
    nums[i] = unique[i]
return len(unique)
```
```python
unique = sorted(set(nums))
nums[:] = unique   #unique che all elements nums madhe update karto (In-place)
return len(unique)
```
> example:  
> input -> nums = [1, 1, 2, 2, 3, 3]  
> set([1, 1, 2, 2, 3, 3]) → {1, 2, 3} #Note: `set` does not maintain order.  
> sorted({1, 2, 3}) → [1, 2, 3]  
> Final unique = [1, 2, 3]  
> nums[:] = unique  → nums = [1, 2, 3]


## 3) Optimized - Two-Pointer Approach (O(n) time, O(1) space)  

> **Idea Behind This Approach:**  
> nums sorted आहे, म्हणजे जर duplicate असेल तर ते back-to-back असतील.  
> दोन pointers वापर:  
> i: unique elements track करतो (slow)  
> j: पुढचे elements scan करतो (fast)  
> जेव्हा nums[j] वेगळा असेल nums[i] पेक्षा, तेव्हा तो नवीन unique element आहे.  
> i ला एक step पुढे नेतो आणि nums[j] ते nums[i] ला assign करतो.  

```python
if not nums: return 0  
i = 0   # slow pointer - points to the last unique element
for j in range(1, len(nums)):  
    if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]  
return i + 1  # length of unique elements
```
