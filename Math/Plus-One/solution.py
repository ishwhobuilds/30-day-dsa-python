from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Current Approach: Convert list to number, add 1, then convert back to list
        num=0
        for i in digits:
            num=(num*10)+i
        num+=1
        new_list=[]
        while num>0:
            rem=num%10
            new_list.append(rem)
            num=num//10
        new_list=new_list[::-1]
        return new_list

    """
    Alternative Approach: (Manual Carry - More Optimal)
    Instead of converting to a big number, we can start from the end:
    
    1. Start from the last digit (right-to-left).
    2. If the digit is less than 9:
       - Just add 1 and return the list (we are done!).
    3. If the digit is 9:
       - Change it to 0 and move to the next digit.
    4. If we finish the loop and everything was a 9 (like [9, 9]):
       - It becomes [0, 0]. Just add a '1' at the start to get [1, 0, 0].

    Example Code:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
    """


        