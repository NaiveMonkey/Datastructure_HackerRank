"""
 Reverse a linked list
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

def Reverse(head):
    if head is None or head.next is None:
        return head
    remaining = Reverse(head.next)
    head.next.next = head
    head.next = None
    return remaining

head = Node(2, None)
head.next = Node(3, None)

head = Reverse(head)

while head is not None:
    print(head.data)
    head = head.next