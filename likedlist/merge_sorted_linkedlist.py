"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def MergeLists(headA, headB):
    if headA is None and headB is None:
        return None

    if headA is None:
        return headB

    if headB is None:
        return headA

    if headA.data < headB.data:
        newNode = headA
        newNode.next = MergeLists(headA.next, headB)

    else:
        newNode = headB
        newNode.next = MergeLists(headA, headB.next)

    return newNode
