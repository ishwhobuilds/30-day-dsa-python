# My Approach (Maximum Subarray)

Kadane's algorithm. I'll just iterate through the array once and keep track of the current maximum sum.

### My Steps:
1.  **Iterate through the array:** Start with the first element.
2.  **Make a choice:** For each element, should I "add it to my existing sum" or "start a new subarray" starting right from this number?
3.  **Update current:** If starting a new one is better (because the old sum was negative), I'll just restart.
4.  **Track the best:** Have a global `max_sum` that I update every time `current_sum` grows.

**Complexity:**
- **Time:** O(n) One linear scan.
- **Space:** O(1) just a few variables.
