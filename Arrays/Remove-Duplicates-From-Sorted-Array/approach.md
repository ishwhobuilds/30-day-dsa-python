# Remove Duplicates from Sorted Array

The array is already sorted, so duplicates are always next to each other. I need to remove them in-place.

### My Approach:
I use two pointers. One pointer (`r`) goes through every element in the array. The other pointer (`l`) keeps track of where the next unique element should go.
Since the first element is always unique, I start `l` at 1. Every time I find a number that is different from the one before it, I move it to the `l` position and increment `l`.

**Complexity:**
- Time: O(n) - Single pass through the array.
- Space: O(1) - No extra space used besides pointers.