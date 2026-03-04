# Pascal's Triangle

The goal is to generate the first few rows of Pascal's Triangle. This is a pattern of numbers where each number is the sum of the two numbers directly above it!

### My Approach:
I decided to build it row by row!
1. For each row, I start by creating a list of ones. Since the first and last numbers are always 1, this makes everything easier.
2. If the row has middle numbers (anything from the second position up to the one before last), I look back at the previous row.
3. I take the two numbers directly above it (`triangle[i-1][j-1]` and `triangle[i-1][j]`) and add them together.
4. Once the row is complete, I just add it to my final triangle list.

### Alternative Way:
There’s a clever little trick you can use! For any row (let’s call it `prev`), the next row can be calculated by doing `[0] + prev` and `prev + [0]`, then adding them together element by element. 
For example, if the previous row is `[1, 2, 1]`, you'd add:
   `[0, 1, 2, 1]`
+  `[1, 2, 1, 0]`
=  `[1, 3, 3, 1]`
It’s a very elegant way to skip the middle calculation loop!

**Complexity:**
- **Time:** O(numRows²) - We have to calculate every number in the triangle.
- **Space:** O(numRows²) - We store all the rows we generate.
