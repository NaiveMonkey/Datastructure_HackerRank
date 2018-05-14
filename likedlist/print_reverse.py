"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def ReversePrint(head):
    if head is not None:
        head.next = ReversePrint(head.next)
        print(head.data)

head = Node(2, None)
head = Node(3, head)
head = Node(1, head)

while head is not None:
    print(head.data)
    head = head.next