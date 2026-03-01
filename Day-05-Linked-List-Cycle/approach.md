# Approach (Linked List Cycle)

Floyd's Tortoise and Hare approach. If you have two runners on a circular track and one is twice as fast as the other, they'll eventually meet again.

### My Steps:
1.  **Set pointers:** One is `slow` (jumps 1 node) and one is `fast` (jumps 2 nodes).
2.  **Move them:** If they ever reference the exact same node, then it's a loop.
3.  **End Check:** If the `fast` pointer hits the end, it's not a cycle.

**Complexity:**
- **Time:** O(n) Either hits the end or meets the other runner.
- **Space:** O(1) Only two extra pointers used.
