# Longest Common Prefix

I need to find the longest string that is at the start of every word in the list.

### My Approach:
I look at the characters of all the words at the same time, starting from the first character. I use the first word as my reference. For each position, I check if all other words have the same character. 
If I find a word that is shorter than the current index, or a character that doesn't match, I stop and return everything I've collected so far.

**Complexity:**
- Time: O(S) - where S is the total number of characters in all strings.
- Space: O(1) - I'm not using any extra space that grows with the input size (just the result string).
