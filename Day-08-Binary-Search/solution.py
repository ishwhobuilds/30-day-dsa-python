# 704. Binary Search
# https://leetcode.com/problems/binary-search/

def search(nums, target):
    # I'll use two pointers: left and right.
    # Check the middle element.
    # If it's too high, move the right pointer left.
    # If it's too low, move the left pointer right.
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            # Look in the left half
            right = mid - 1
        else:
            # Look in the right half
            left = mid + 1
            
    # Target not found
    return -1

# Test
# print(search([-1, 0, 3, 5, 9, 12], 9)) # 4
