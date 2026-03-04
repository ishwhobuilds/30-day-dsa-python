# Merge Sorted Array

The goal is to merge two sorted arrays into one. We already have enough space at the end of the first array (`nums1`) to hold everything.

### My Approach:
I decided to work backwards! We know the largest numbers should go at the very end of the array, so it’s easier to compare the biggest elements of both lists and place them starting from the last available spot.
1. I set up three pointers: one for the end of the actual numbers in `nums1`, one for the end of `nums2`, and one for where the next number should go in the final combined array.
2. I compare the numbers from the back. If the number in `nums1` is bigger, I move it to the back. If the number in `nums2` is bigger, I move that one instead.
3. I keep going until all numbers from `nums2` are placed. Since `nums1` is already sorted, once `nums2` is empty, we’re done!

### Alternative Way:
A very easy (but less efficient) way would be to simply copy all the numbers from `nums2` into the empty spaces of `nums1` and then sort the whole thing at once using `nums1.sort()`. 
While this is super simple to write, it's a bit slower because sorting an entire array takes more effort than just merging two sorted parts.

**Complexity:**
- **Time:** O(m + n) - We only go through each number once.
- **Space:** O(1) - We are doing everything "in-place," so we don't need any extra lists!
