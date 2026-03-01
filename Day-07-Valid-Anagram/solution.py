# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

def isAnagram(s: str, t: str) -> bool:
    # If the lengths aren't same, they can't be anagrams.
    # I'll use a dictionary to count occurrences of each character in s.
    # Then I'll subtract them as I see characters in t.
    if len(s) != len(t):
        return False
        
    counts = {}
    
    # Increment counts for each char in s
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        
    # Decrement counts for each char in t
    for char in t:
        if char not in counts:
            return False
        counts[char] -= 1
        if counts[char] < 0:
            return False
            
    # All counts should be zero if it's an anagram
    return True

# Test
# print(isAnagram("anagram", "nagaram")) # True
