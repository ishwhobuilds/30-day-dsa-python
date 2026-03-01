# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

def isValid(s: str) -> bool:
    # I'll use a stack to keep track of opening brackets.
    # When I hit a closing bracket, it has to match the last one I opened.
    stack = []
    lookup = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in lookup:
            # It's a closing bracket
            if stack and stack[-1] == lookup[char]:
                stack.pop()
            else:
                return False
        else:
            # It's an opening bracket, just push it
            stack.append(char)
            
    # If the stack is empty, every bracket was closed correctly
    return not stack

# Test
# print(isValid("()[]{}")) # True
