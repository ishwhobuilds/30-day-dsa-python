# Best Time to Buy and Sell Stock

The goal is to find the maximum profit you can make from buying and selling a stock. You can only buy once and sell once, and you must buy before you sell!

### My Approach:
I decided to imagine I'm walking through the stock prices day by day.
1. I keep track of the **lowest price** I've seen so far. That’s my potential "buy" price.
2. For every new price, I check:
   - Is this lower than my current lowest? If so, I update my lowest price (because I'd rather buy cheaper!).
   - If I were to sell at today's price, would I make more profit than my current record? If yes, I update my maximum profit.
3. By the end, I'll have the biggest profit possible!

### Alternative Way:
A more advanced way to think about this is called **Kadane’s Algorithm**. Instead of tracking the min price, you can track the "difference" between each day's price and look for the maximum sum of those differences.
However, for this specific problem, the `min_price` and `max_profit` approach (the one you used) is the cleanest and most straightforward!

**Complexity:**
- **Time:** O(n) - We only walk through the list of prices once.
- **Space:** O(1) - We only keep track of two numbers (`minp` and `maxp`).
