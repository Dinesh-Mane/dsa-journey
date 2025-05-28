# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

## Problem Statement
एक array `prices[]` दिला आहे, जिथे `prices[i]` म्हणजे त्या दिवशीचा stock price आहे.
तुला exactly एकदाच buy आणि एकदाच sell करायचं आहे.
sell करण्याच्या आधीच Buy करायचं आहे (i.e., earlier day).  
Return the maximum profit you can achieve.
If you can’t make any profit, return 0. 

**Constraints:**  
> You can buy and sell only once  
> You must buy before selling   
> Time complexity should ideally be O(n)

**Example**
```python
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```
```python
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Try all pairs ( Time: O(n²), Space: O(1))  
Idea:   
Every possible pair (i, j) where i < j, check profit = prices[j] - prices[i]  
Keep track of max profit.  
> प्रत्येक दिवशी buy करून त्यानंतरच्या प्रत्येक दिवशी sell करून profit काढायचा.
> सगळ्यात जास्त profit कोणता आहे ते शोधायचं.

```python
max_profit = 0
for i in range(len(prices)):
  for j in range(i+1, len(prices)):
    profit = prices[j] - prices[i]
    max_profit = max(max_profit, profit)
return max_profit
```
## 2) Optimized - One Pass (Tracking `Min price` & `max profit`) (O(n) time, O(1) space)  

> **Idea Behind This Approach:**  
> प्रत्येक दिवसाचा भाव तपासा.
> आतापर्यंतचा सर्वात स्वस्त भाव लक्षात ठेवा (min_price).
> त्या दिवसाचा भाव वापरून profit काढा (price - min_price).
> जो सर्वाधिक असेल तो max_profit म्हणून ठेवा.

रोजचा भाव बघ → minimum price update कर → त्या दिवशीचा profit काढ → max_profit update कर

```python
min_price = float('inf')
max_profit = 0
for price in prices:
  min_price = min(min_price, price)
  max_profit = max(max_profit, price - min_price)
return max_profit
```

