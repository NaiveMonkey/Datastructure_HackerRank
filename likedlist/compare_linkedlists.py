"""
 Merge two linked list
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


def CompareLists(headA, headB):

    while headA and headB:
        print(str(headA.data) + " : " + str(headB.data))
        if headA.data == headB.data:
            headA = headA.next
            headB = headB.next
        else:
            return 0
    if headA is None and headB is None:
        return 1
    return 0

headA = Node(1, None)
headA.next = Node(2, None)
headA.next.next = Node(3, None)

headB = Node(1, None)
headB.next = Node(2, None)

CompareLists(headA, headB)