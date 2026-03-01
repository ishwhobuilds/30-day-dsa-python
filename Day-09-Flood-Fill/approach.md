# My Approach (Flood Fill)

I'll use a Depth-First Search (DFS) for this one. It's exactly like the paint bucket tool in an image editor.

### My Steps:
1.  **Check initial color:** If the current pixel already matches the new color, there's nothing for me to do. 
2.  **Define DFS function:** It'll check if the current pixel's color matches the starting color.
3.  **Color the pixel:** If it matches, swap the color.
4.  **Repeat for neighbors:** Look Up, Down, Left, and Right (4-way connectivity) and call the same function on those coordinates.

**Complexity:**
- **Time:** O(N) where N is the total number of pixels in the grid (at most we visit each pixel once).
- **Space:** O(N) recursion stack for the worst-case scenario.
