# Plus One

The goal is to take a list of digits representing a large number, add 1 to it, and return the new list of digits.

### My Approach:
I decided to keep it simple! I first converted the entire list of digits into a single integer. For example, if I have `[1, 2, 3]`, I turn it into `123`. 
Then, I simply add 1 to that number (making it `124`). 
Finally, I break that number back down into individual digits and put them into a new list. It's like doing math how we normally would!

### Alternative Way:
There's another cool way to do this without converting the whole thing to a big number. We can start from the end (the right-most digit) and add 1 manually.
1. If the last digit is less than 9, just add 1 and we are done!
2. If it's 9, it becomes 0, and we carry over 1 to the next digit to the left.
3. We keep doing this until we find a digit that isn't 9. 
4. If all the digits were 9 (like `999`), we'd end up with `000` and just add a `1` at the very beginning to get `1000`.

**Complexity:**
- **Time:** O(n) - We go through the list once.
- **Space:** O(n) - We are creating a new list for the result.
