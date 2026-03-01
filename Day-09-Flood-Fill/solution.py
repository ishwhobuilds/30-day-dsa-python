# 733. Flood Fill
# https://leetcode.com/problems/flood-fill/

def floodFill(image, sr, sc, color):
    # Get the initial color we're replacing.
    # If the target is already that color, we're done.
    # Otherwise, use recursive DFS to fill neighbors.
    start_color = image[sr][sc]
    
    # Base check
    if start_color == color:
        return image
        
    R, C = len(image), len(image[0])
    
    def dfs(r, c):
        if 0 <= r < R and 0 <= c < C and image[r][c] == start_color:
            # Change the color
            image[r][c] = color
            # Recurse in all four directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
    dfs(sr, sc)
    return image

# Test case
# print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
# Output: [[2,2,2],[2,2,0],[2,0,1]]
