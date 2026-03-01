# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    # I'll keep track of the minimum price I've seen so far.
    # For each price, I'll calculate the potential profit if I sold today.
    # If it's a new max profit, I'll update it.
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Update the minimum price (potential buy date)
        if price < min_price:
            min_price = price
        # Update the profit if selling today is better
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit

# Quick test
# print(maxProfit([7,1,5,3,6,4])) # Output: 5
