# Two Sum

The goal is to find two numbers in the array that add up to a specific target. 

### My Approach:
Instead of checking every possible pair (which would take too long), I use a dictionary to remember every number I've seen so far and its position. 
As I go through the array, I calculate what number I need to reach the target (target - current number). If that "needed" number is already in my dictionary, I've found the pair!

**Complexity:**
- Time: O(n) - I only go through the list once.
- Space: O(n) - In the worst case, I store almost every number in my dictionary.
