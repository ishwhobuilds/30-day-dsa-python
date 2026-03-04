# Single Number

The goal is to find the one number in a list that doesn't have a pair. Every other number appears exactly twice!

### My Approach:
I used a bit of "magic" called the **XOR (^) operator**! 
1. XOR is a special operator where if you XOR a number with itself, you get 0 (e.g., `5 ^ 5 = 0`).
2. If you XOR a number with 0, you get the number itself (e.g., `5 ^ 0 = 5`).
3. So, by XORing every number in the list together, all the pairs cancel each other out, and only the "lonely" single number is left at the end. It's super fast and efficient!

### Alternative Way:
You could also use a **Hash Map (a dictionary in Python)** to count how many times each number appears. Then, you just look for the one with a count of 1.
While this is easy to understand, it's not as "neat" as the XOR trick because storing a dictionary takes up extra memory (Space Complexity).

**Complexity:**
- **Time:** O(n) - We only go through the list once.
- **Space:** O(1) - We only need one variable (`ans`) to store our result!
