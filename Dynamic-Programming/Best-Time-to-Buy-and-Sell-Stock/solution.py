from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')  # Start with a very high price
        maxp = 0
        for price in prices:
            # If we find a lower price than before, let's "buy" it here!
            if price < minp:
                minp = price
            # Or if selling at the current price gives us more profit than before, update maxp
            elif price - minp > maxp:
                maxp = price - minp
        return maxp
