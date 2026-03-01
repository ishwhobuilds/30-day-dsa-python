# My Approach (Binary Search)

A simple binary search. Since the input array is already sorted, I can find the target in logarithmic time instead of scanning everything.

### My Steps:
1.  **Define pointers:** `left` (0) and `right` (end of array). 
2.  **Calculate the middle:** Check if the element at `middle` is the target.
3.  **Narrow the search:** If it's not the target, either the target is in the left half or the right half.
4.  **Repeat:** Keep cutting the array in half until I find it or until the pointers cross.

**Complexity:**
- **Time:** O(log n) No more linear scans.
- **Space:** O(1) Just a couple of variables to keep track of the indices.
