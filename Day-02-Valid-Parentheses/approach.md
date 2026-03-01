# Logic behind my solution (Valid Parentheses)

I need to make sure brackets are closed in the right order. A stack is perfect here because common practice is "last in, first out."

### My Steps:
1.  **Iterate through the string:** Check each character one by one.
2.  **Handle Opening Brackets:** If it's one of `(`, `{`, or `[`, I just toss it onto my stack.
3.  **Handle Closing Brackets:** When I see something like `)`, I check if the stack actually has its pair `(`. If it does, I pop it. If it doesn't match or the stack is empty, it's already an invalid string, so I return `False` immediately.
4.  **Final Check:** At the very end, if the stack is completely empty, it means everything was closed properly.

**Complexity:**
- **Time:** O(n) Since I'm just going through the string once.
- **Space:** O(n) Worst case, the string has only opening brackets and they all end up on the stack.
