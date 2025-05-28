# [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

## Problem Statement
You are given an array `prices[]` where `prices[i]` is the price of a stock on day `i`.  
You can buy and sell the stock multiple times (but not multiple stocks at once).    
**Your goal: Maximize total profit**  
> एका दिवसात फक्त एक stock विकत घेता येतो किंवा विकता येतो  
> एकाच वेळी multiple transactions allowed नाहीत, पण एक विकल्यावर लगेच दुसरा खरेदी करता येतो.  

**Constraints:**  
Only one valid pair will exist.  
You can't use the same element twice (i.e., don’t reuse index).  
Return the indices, not the values.  

**Example**
```python
Input: prices = [7,1,5,3,6,4]
Output: 7

Explanation: 
Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 4  
Buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 3  
Total profit = 4 + 3 = 7
```
```python
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
```
```python
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Try all combinations ( Time: O(2^n) — very slow, Space: O(n))  
Idea: Try all possible buy/sell combinations recursively.  

```python
def helper(i, holding):
  if i == len(prices): return 0
  profit = helper(i + 1, holding)  # Choice 1: Do nothing
  if holding: profit = max(profit, prices[i] + helper(i + 1, False))  # Choice 2: Sell today
  else: profit = max(profit, -prices[i] + helper(i + 1, True))  # Choice 3: Buy today
  return profit
return helper(0, False)
```
## 2) Peak-Valley Approach (O(n) time, O(1) space)  
**Logic:**  
Find every increasing segment: buy at valley, sell at peak.  
Add profit of each such transaction.  
```python
i = 0
profit = 0
while i < len(prices) - 1:
  while i < len(prices)-1 and prices[i] >= prices[i+1]: i += 1
  buy = prices[i]
  while i < len(prices)-1 and prices[i] <= prices[i+1]: i += 1
  sell = prices[i]
  profit += sell - buy
return profit
```

## 3) Optimized - Greedy Solution (O(n) time, O(1) space)  
**Idea:** जेव्हा price increase होतं (i.e. prices[i+1] > prices[i]) तेव्हा आपण profit कमवू शकतो. म्हणून जिथे जिथे increase आहे तिथे तितका profit add करा.  
> We don't need to track exact buy/sell days. Just add all upward differences

```python
profit = 0
for i in range(1, len(prices)):
  if prices[i] > prices[i - 1]: profit += prices[i] - prices[i - 1]
return profit
```