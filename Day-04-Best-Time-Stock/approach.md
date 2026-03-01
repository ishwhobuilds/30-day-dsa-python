# My Approach (Best Time to Buy and Sell Stock)

I want to find the biggest gap between a "high" and a "low," but the low has to come before the high. 

### My Steps:
1.  **Keep track of the Minimum Price:** As I go through the list, I'll update the minimum price I've ever seen.
2.  **Calculate Potential Profit:** If I see a price that's higher than my minimum, I'll calculate the gap.
3.  **Update Max Profit:** If this gap is bigger than the previous `max_profit`, I'll update it.

**Complexity:**
- **Time:** O(n) One linear scan.
- **Space:** O(1) Only storing `min_price` and `max_profit`.
