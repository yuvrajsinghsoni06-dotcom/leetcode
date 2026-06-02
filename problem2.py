class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init(self):
        self.head = None
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def remove_elel_nth_position(self,position):
        if self.head is None:
            return 
        if position == 0:
            self.head = self.head.next
            return 
        current = self.head
        for i in range(position-1):
            if current.next is None:
                return 
            current = current.next
        current.next = current.next.next
        
    

if  __name__ == "__main__":
    l1 = LinkedList()
    l1.head = Node(1)
    l1.head.next = Node(2)
    l1.head.next.next = Node(3)
    l1.head.next.next.next = Node(4)
    l1.display()
    l1.remove_elel_nth_position(3)
    l1.display()
        
