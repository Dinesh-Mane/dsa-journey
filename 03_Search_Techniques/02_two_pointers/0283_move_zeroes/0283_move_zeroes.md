# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/description/)

## Problem Statement
Given an integer array nums, move all 0's to the end without changing the relative order of the non-zero elements.  
> Do it in-place with O(1) extra space and try to minimize the total number of operations.  

**Example**
```python
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```
```python
Input: nums = [0]
Output: [0]
```
> Zeroes नंतर ढकलायचे आहेत आणि बाकीचे क्रम टिकवायचे आहेत. म्हणजेच non-zero values ला पुढे आणायचं आणि उरलेली जागा 0 ने भरायची.

## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – using extra array (Not in-place) (O(n²) time, O(1) space)
```python
res = []
for n in nums:
    if n != 0: res.append(n)
while len(res) < len(nums): res.append(0)
for i in range(len(nums)): nums[i] = res[i]
```
apann ithe `while len(res) < len(nums): res.append(0)` chya jagi `no. of zeros` cha count kadhun direct ek line madhe **extend** karu shakto , like this 
```python
zero_count = len(nums) - len(res)
res.extend([0] * zero_count)
# or like this
res.extend([0] * (len(nums) - len(res)))
```
ani apann `for i in range(len(nums)): nums[i] = res[i]` chya jagi direct asa lihu shakto `nums[:] = res`   

## 1) Dusri method – using extra array (Not in-place) 
```python
res = [0]*len(nums)
i=0
for n in nums:
    if n != 0: 
        res[i] = n
        i+=1
nums[:] = res
```
## 2) Two-pass Approach (In-place, O(n) time, O(1) space)
**Idea:**  
1st pass: Copy non-zero elements to the front  
2nd pass: Fill rest of array with zeroes  
```python
j = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j] = nums[i]
        j += 1
for i in range(j, len(nums)): nums[i] = 0
```
## 3) Optimized - Swap Method - Single Pass (O(n) time, O(1) space)
> **Idea Behind This Approach:**    
> `i` म्हणजे loop index, `j` म्हणजे non-zero value ठेवायची जागा.  
> जर `nums[i] ≠ 0` असेल, तर त्याला `nums[j]` शी swap करा.  
> हे करायचं कारण म्हणजे `0` च्या जागी non-zero घालायचा आणि `0` मागे ढकलायचं.  

```python
j = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
```
