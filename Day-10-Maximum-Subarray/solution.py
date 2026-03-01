# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
    # I'll use a local maximum and a global maximum.
    # For each number, I'll either add it to the current subarray or start fresh.
    # This is basically Kadane's algorithm.
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Decide if we're adding the current number or starting from it
        current_sum = max(nums[i], current_sum + nums[i])
        # Update our global best
        max_sum = max(max_sum, current_sum)
        
    return max_sum

# Quick test
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
