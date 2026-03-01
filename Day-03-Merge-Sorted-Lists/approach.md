# Approach (Merge Two Sorted Lists)

I'll just merge these like two sorted stacks of paper. I'll always take the smaller value from the two available lists and move that pointer.

### My Steps:
1.  **Use a Dummy Node:** It avoids handling "what's the head" as a special case.
2.  **Compare Each Element:** As long as both `list1` and `list2` have nodes, I'll grab the smaller one and point my `current` node to it.
3.  **Move the Corresponding Pointer:** Once something's merged, that pointer needs to move forward.
4.  **Append remaining:** If one list is longer, I'll just attach the leftover part.

**Complexity:**
- **Time:** O(n + m), where `n` and `m` are the lengths of both lists.
- **Space:** O(1) Actually just rearranging the pointers instead of creating a whole new list.
