"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method
"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    if head is None:
        head = Node(data, None)
        return head
    else:
        head.next = Insert(head.next, data)
    return head


head = Insert(None, 4)
head = Insert(head, 5)
head = Insert(head, 2)

while head is not None:
    print(head.data)
    head = head.next