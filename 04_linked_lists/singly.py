class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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
    
    def delete(self, value):
        curr = self.head

        if curr is None:
            print("list is empty")
            return 
        
        if curr.data == value:
            self.head = curr.next
            return
        
        prev = None
        while curr is not None and curr.data != value:
            prev = curr
            curr = curr.next

        if curr is None:
            print("value not found")
        else:
            prev.next = curr.next

    def display(self):
        print("list display")
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("none")

if __name__ == "__main__":
    sll = SinglyLinkedList()

    sll.insert_front(10)
    sll.insert_front(20)
    sll.insert_end(30)
    sll.insert_end(40)

    sll.display()
    
    sll.delete(30)
    sll.display()