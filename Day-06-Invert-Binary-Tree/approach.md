# My Approach (Invert Binary Tree)

This is basically building a mirror image of the tree. I'll just swap the left and right children for every single node.

### My Steps:
1.  **Iterate or Recurse:** I chose recursion because trees have a recursive structure anyway.
2.  **Base Case:** If the node is `None`, there's nothing left to swap. 
3.  **Swap:** I swap the left and right child pointers.
4.  **Repeat:** For each of the children, I repeat the same process until the entire tree is inverted.

**Complexity:**
- **Time:** O(n) visiting every single node.
- **Space:** O(h) where `h` is the height of the tree (recursion stack).
