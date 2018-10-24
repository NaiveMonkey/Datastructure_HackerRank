"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
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

def Insert(head, data):
    newNode = Node(data, Node)
    newNode.next = head
    return newNode

head = Insert(None, 2)
head = Insert(head, 5)
head = Insert(head, 3)

while head is not None:
    print(head.data)
    head = head.next