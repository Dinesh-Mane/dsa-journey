# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)

## Problem Statement
You're given a string s containing just the characters: `'(', ')', '{', '}', '[', ']'`  
Your task is to check if the input string is valid.

#### A string is considered valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding open bracket.

**Example**
```python
Input: s = "()"
Output: True

Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False

Input: s = "([)]"
Output: False

Input: s = "{[]}"
Output: True
```

## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach — Repeated Replacement ( Time: O(n²), Space: O(n))  
Idea:   
1. While s contains any of `"()"`, `"[]"`, or `"{}"`, keep replacing them with `""`.
2. If at the end, `s` becomes an empty string → it's valid. Otherwise, invalid.

```python
while '()' in s or '{}' in s or '[]' in s:
  s = s.replace('()', '').replace('{}', '').replace('[]', '')
return s == ''
```

## 2) Stack with Incorrect Mapping (O(n) time, O(n) space)  
**Idea:**  
1. Push every opening bracket into a stack.  
2. When you see a closing bracket, check if it matches the last one in the stack.  
3. But you hardcode if `x == '(' and y == ')'` for every type.  

```python
st = []
for c in s:
  if c in '({[': st.append(ch)
  else:
    if not st: return False
    top = st.pop()
    if c==')' and top !='(': return False
    if c=='}' and top !='{': return False
    if c==']' and top !='[': return False
return not st
```

## 3) Stack with Mapping Dictionary (O(n) time, O(n) space)  
**Idea:** Use a stack and a dictionary of matching pairs:
```python
pairs = {')': '(', '}': '{', ']': '['}
```
For every char in string:  
- If it's a closing bracket → check if the last item in stack is its pair.
- Else push to stack.

If stack is empty at end → valid.
```python
st = []
mapp = {')': '(', '}': '{', ']': '['}
    
for c in s:
  if c in mapp:
    top = st.pop() if st else '#'
    if mapp[c] != top: return False
  else: st.append(c)
return not st
```
> This is the most common solution seen in interviews.

## 4) Reverse Logic – Push Expected Closing Bracket (Time: O(n), Space: O(n))
**Idea:** Instead of storing opening brackets, store what closing bracket we expect.  
So:
- On `'('`, push `')'`
- On `'['`, push `']'`
- On `'{'`, push `'}'`

Then, when we encounter a closing bracket, check if it matches stack.pop()

```python
st = []
for c in s:
  if c == '(': st.append(')')
  elif c == '{': st.append('}')
  elif c == '[': st.append(']')
  else:
    if not st or st.pop() != c: return False
return not stack
```