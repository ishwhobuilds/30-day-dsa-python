# Search Insert Position

I need to find the index where a target value should be in a sorted array. If it's already there, return the index; otherwise, return where it would be inserted.

### My Approach:
Since the array is already sorted, binary search is the way to go. I keep narrowing down the range by checking the middle element. 
If the target is smaller than the middle, I look in the left half. If it's larger, I look in the right half. Eventually, if I don't find it, the "left" pointer will be at the correct insertion index.

**Complexity:**
- Time: O(log n) - Binary search efficiency.
- Space: O(1) - Just using a few pointers.