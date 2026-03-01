# My Approach (Valid Anagram)

I need to make sure both strings have the exact same characters and the exact same counts.

### My Steps:
1.  **Check Length:** If they don't have the same length, they're obviously not anagrams.
2.  **Count Occurrence:** I'll use a dictionary (hash map) to count how many times each character appears in string `s`.
3.  **Cross-Check:** Now, for each character in string `t`, I'll reduce the count in the dictionary. 
4.  **Validate:** If the character isn't there, or if the count drops below zero, it's not an anagram. 

**Complexity:**
- **Time:** O(n + m) for counting characters.
- **Space:** O(1) Actually limited to 26 characters if it's just lowercase letters.
