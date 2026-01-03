class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def delete(self, value):
        curr = self.head

        while curr is not None and curr.data != value:
            curr = curr.next

        if curr is None:
            print("value not found")
            return
        
        if curr is self.head and curr is self.tail:
            self.head = self.tail = None
            return

        if curr is self.head:
            self.head = curr.next
            self.head.prev = None
            return
        
        if curr is self.tail:
            self.tail = curr.prev
            self.tail.next = None
            return
        
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

    def display(self):
        print("list display")
        print("None", end=" <-> ")

        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next

        print("None")

if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_front(10)
    dll.insert_front(20)
    dll.insert_end(30)
    dll.insert_end(40)

    dll.display()
    
    dll.delete(30)
    dll.display()