# [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=hash-table)

## Problem Statement
Given an integer, convert it to a Roman numeral.
- Valid for 1 <= num <= 3999
- Use proper Roman numeral rules (subtractive notation, ordering, etc.)

---

## Examples

```
Input: num = 3749
Output: "MMMDCCXLIX"
Explanation:
3000 = MMM, 700 = DCC, 40 = XL, 9 = IX

Input: num = 58
Output: "LVIII"
Explanation:
50 = L, 8 = VIII

Input: num = 1994
Output: "MCMXCIV"
Explanation:
1000 = M, 900 = CM, 90 = XC, 4 = IV
```

---

## Solution 1: Brute Force Using Conditions
**Idea:** Subtract each Roman value manually using conditional blocks.

```python
def intToRoman(num):
    res = ""
    while num >= 1000:
        res += "M"
        num -= 1000
    while num >= 900:
        res += "CM"
        num -= 900
    while num >= 500:
        res += "D"
        num -= 500
    while num >= 400:
        res += "CD"
        num -= 400
    while num >= 100:
        res += "C"
        num -= 100
    while num >= 90:
        res += "XC"
        num -= 90
    while num >= 50:
        res += "L"
        num -= 50
    while num >= 40:
        res += "XL"
        num -= 40
    while num >= 10:
        res += "X"
        num -= 10
    while num >= 9:
        res += "IX"
        num -= 9
    while num >= 5:
        res += "V"
        num -= 5
    while num >= 4:
        res += "IV"
        num -= 4
    while num >= 1:
        res += "I"
        num -= 1
    return res
```

- Time: O(n) for n in Roman digits
- Space: O(1)

---

## Solution 2: Using Value-Symbol Mapping
**Idea:** Use a descending value-symbol pair list and subtract greedily.

```python
def intToRoman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""
    for i in range(len(val)):
        while num >= val[i]:
            res += syms[i]
            num -= val[i]
    return res
```

- Time: O(n)
- Space: O(1)
- ✅ More structured than solution 1

---

## Solution 3: Compressed Using Zip
**Idea:** Use zip() on value-symbol list to make the code cleaner.

```python
def intToRoman(num):
    val_sym = zip(
        [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
        ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    )
    res = ""
    for val, sym in val_sym:
        count, num = divmod(num, val)
        res += sym * count
    return res
```

- Time: O(1) because max 13 symbols in loop
- Space: O(1)
- ✅ Concise and optimal

---

## Solution 4: Dictionary with divmod()
**Idea:** Use dictionary and loop with divmod for performance.

```python
def intToRoman(num):
    table = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }
    res = ""
    for val in sorted(table.keys(), reverse=True):
        count, num = divmod(num, val)
        res += table[val] * count
    return res
```

- Time: O(1)
- Space: O(1)
- ✅ Dictionary may feel intuitive for mapping

---

## Optimal Solution (Recommended for Interviews)
**Solution 3 (Zip + Greedy with divmod)** is:
- ✅ Clean
- ✅ Optimal
- ✅ Easy to write & explain in interviews

---

## Hints for Similar Problems
1. Always **greedily subtract** the largest possible Roman symbol
2. Watch out for **subtractive forms**: 4, 9, 40, 90, etc.
3. Pre-map values and loop greedily
4. `divmod()` helps you extract how many times a Roman symbol fits
5. Stick to order: M, CM, D, CD, ..., IV, I