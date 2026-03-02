# Remove Element

I need to remove all occurrences of a specific value from the array in-place.

### My Approach:
I use a two-pointer technique. I iterate through the array with a fast pointer (`r`). If the current element is not the value I want to remove, I copy it to the position of the slow pointer (`l`) and move the slow pointer forward. 
This way, all the "good" elements are shifted to the front of the array.

**Complexity:**
- Time: O(n) - I check each element once.
- Space: O(1) - Modified the array in-place.