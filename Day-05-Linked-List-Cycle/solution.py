# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    # I'll use Floyd's Tortoise and Hare algorithm.
    # Basically, two pointers moving at different speeds.
    # If there's a cycle, the fast pointer will eventually catch the slow one.
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # If they meet, there's a cycle
        if slow == fast:
            return True
            
    # If we made it to the end, there's no cycle
    return False
