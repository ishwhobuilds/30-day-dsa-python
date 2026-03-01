# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# List node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # I'll create a dummy node to stay sane while pointing to the new list.
    # It just makes handling the head of the list way easier.
    dummy = ListNode()
    curr = dummy
    
    # Iterate as long as both lists have nodes
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
        
    # If one of the lists is already empty, just attach the rest of the other one
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2
        
    return dummy.next
