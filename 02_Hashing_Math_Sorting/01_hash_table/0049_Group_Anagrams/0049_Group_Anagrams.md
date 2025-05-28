# [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/description/)

## Problem Statement
You are given an array of strings `strs`. Group the anagrams together. You can return the answer in any order.
> An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.


**Example**
```python
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
```
```python
Input: strs = [""]
Output: [[""]]
```
```python
Input: strs = ["a"]
Output: [["a"]]
```

**Goal:** Group all anagrams together from the input list.

## Possible Solutions – Brute Force to Optimized
## 1) Brute Force – Compare each with all others (O(n² * k log k) Time, O(n) Space)
**Idea:** 
- For each string, compare it with every other.
- Check if both are anagrams by sorting and comparing.
- Group them manually (use a visited array to avoid re-checking).

```python
visited = [False] * len(strs)
res = []

for i in range(len(strs)):
  if visited[i]: continue
  temp = [strs[i]]
  visited[i] = True
  for j in range(i+1, len(strs)):
    if sorted(strs[i]) == sorted(strs[j]):
      temp.append(strs[j])
      visited[j] = True
  res.append(temp)
return res
```
**Why it's slow:**
- Sorting every time inside the loop (O(k log k))
- Repeated comparisons (O(n²))

## 2) HashMap with Sorted String as Key (O(n * k log k) Time, O(n * k) Space)
**Idea:** 
- Anagrams become equal after sorting (e.g., "eat" → "aet", "tea" → "aet")
- Use a dictionary with the sorted string as the key
- Append words into the corresponding list

```python
res = defaultdict(list)
for w in strs:
  key = ''.join(sorted(w))  # sort karun parat string madhe convert karat ahe
  res[key].append(w)
return list(res.values())
```
> Pros: Fast and easy to implement, Clean structure and Most commonly accepted in interviews

## 3) HashMap with Count Tuple (No Sort) – Optimized (O(n * k) Time, O(n * k) Space)
**Idea:**  
1. Instead of sorting, count how many times each character appears (26-length list for 'a' to 'z')
2. Use the count tuple as key since it uniquely identifies an anagram group

```python
res = defaultdict(list)
for w in strs:
  cnt = [0]*26
  for c in w:
    cnt[ord(c)-ord('a')]+=1
  key = tuple(cnt)
  res[key].append(w)
return list(res.values())
```
**Why this is better:**
- Avoids sorting (k log k → becomes just k)
- Works faster for longer strings

> Best Optimized Approach for Interviews

## OR Using `collections.Counter` – Readable Alternative (O(n * k) Time, O(n * k) Space)
**Idea:** Use Counter (dictionary subclass) as the key – but since Counter isn't hashable, convert to a `frozenset` or `tuple`.

```python
res = defaultdict(list)
for w in strs:
  key = tuple(sorted(Counter(w).items()))
  res[key].append(w)
return list(res.values())
```
>  Clean but: Slightly heavier due to Counter object and sorting items