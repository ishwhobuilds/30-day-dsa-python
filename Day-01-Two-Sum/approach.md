# Two Sum - Thoughts

Standard problem, but good for warming up with hash maps.

### My Logic:
Instead of doing a nested loop ($O(n^2)$), I'm just doing one pass. I store every number I see in a dict. If `target - current_number` is already in the dict, I found the pair.

**Complexity:**
- Time: $O(n)$ because of the single loop.
- Space: $O(n)$ for the dictionary storage.

Note: Remember that the problem says exactly one solution exists, so no need to handle edge cases for multiple pairs yet.

