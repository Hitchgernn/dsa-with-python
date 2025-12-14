class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
