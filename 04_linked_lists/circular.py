class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinikedList:
    def __init__(self):
        self.head = None
    
    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next is not self.head:
                curr = curr.next

            new_node.next = self.head
            curr.next = new_node
            self.head = new_node
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        curr = self.head
        while curr.next is not self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head
    
    def delete(self, value):
        curr = self.head

        if curr is None:
            print("list is empty")
            return
        
        if self.head.next is self.head:
            if self.head.data == value:
                self.head = None
            else:
                print("value not found")
            return
        
        while curr.next is not self.head and curr.next.data != value:
            curr = curr.next
        
        if curr.next is self.head:
            if self.head.data == value:
                self.head = curr.next.next
                curr.next = self.head
            else:
                print("value not found")
            return
        
        curr.next = curr.next.next

    def display(self):
        if self.head is None:
            print("list is empty")
            return

        print("list display")
        curr = self.head

        while curr.next != self.head:
            print(curr.data, end=" -> ")
            curr = curr.next

        print(curr.data, end=" -> ")

if __name__ == "__main__":
    cll = CircularLinikedList()

    cll.insert_front(10)
    cll.insert_front(20)
    cll.insert_end(30)
    cll.insert_end(40)

    cll.display()
    
    cll.delete(30)
    cll.display()