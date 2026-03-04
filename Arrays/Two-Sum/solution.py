# Day 1: Two Sum
# Got this one done using a hash map to keep it O(n). 
# Using a dictionary to store seen values and their indices.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val -> index
        
        for i, val in enumerate(nums):
            remaining = target - val
            if remaining in seen:
                return [seen[remaining], i]
            seen[val] = i
        
        return []

# Quick check
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9)) # should be [0, 1]
    print(s.twoSum([3, 2, 4], 6))    # should be [1, 2]

