"""
 Delete Node at a given position in a linked list
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
    if head is None:
        head = Node(data, None)
        return head
    else:
        head.next = Insert(head.next, data)
    return head

def Delete(head, position):
    if position == 0: return head.next
    head.next = Delete(head.next, position - 1)
    print(head.data)
    return head

head = Insert(None, 1)
head = Insert(head, 2)
head = Insert(head, 3)

head = Delete(head, 2)

# while head is not None:
#     print(head.data)
#     head = head.next
