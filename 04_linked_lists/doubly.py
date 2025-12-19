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
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        # actually walker node is smart move here but im trying out something tougher
        while curr.next is not None: 
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

    def delete(self, value):
        curr = self.head

        if curr is None:
            print("list is empyt")
            return
        
        if curr.data == value:
            self.head = curr.next
            if self.head is not None:
                self.head.prev = None
            return 
        
        while curr is not None and curr.data != value:
            curr = curr.next
        
        if curr is None:
            print("value not found")
            return
        
        if curr.next is not None:
            curr.next.prev = curr.prev
        curr.prev.next = curr.next

    def display(self):
        print("list display")
        print("None", end=" <-> ")

        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next

        print("None")

if __name__ == "__main__":
    sll = DoublyLinkedList()

    sll.insert_front(10)
    sll.insert_front(20)
    sll.insert_end(30)
    sll.insert_end(40)

    sll.display()
    
    sll.delete(30)
    sll.display()