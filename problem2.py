class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):  # FIXED: Added missing trailing underscores
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_elel_nth_position(self, position):
        # 1. FIXED: Guardrail for negative positions
        if position < 0:
            print(f"Error: Position {position} is invalid (negative).")
            return

        if self.head is None:
            return 
        
        if position == 0:
            self.head = self.head.next
            return 
        
        current = self.head
        for i in range(position - 1):
            if current.next is None:
                print("Error: Position out of bounds.")
                return 
            current = current.next
        
        # 2. FIXED: Guardrail to ensure the node to delete (current.next) actually exists
        if current is None or current.next is None:
            print("Error: Position out of bounds.")
            return
            
        current.next = current.next.next
        
    # to remove from the end

    def remove_from_end(self,n):
        dummy = Node(0)
        dummy.next = self.head

        p1 = dummy
        p2 = dummy

        for i in range(n):
            p1 = p1.next
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next

        return dummy.next
        
if __name__ == "__main__":
    l1 = LinkedList()
    
    # Manually setting up nodes for testing
    l1.head = Node(1)
    l1.head.next = Node(2)
    l1.head.next.next = Node(3)
    l1.head.next.next.next = Node(4)
    
    print("Original list:")
    l1.display()
    
    # print("\nExecuting: remove_elel_nth_position(-1)")
    # l1.remove_elel_nth_position(-1)  # Handled safely now!
    # l1.display()
    
    # print("\nExecuting: remove_elel_nth_position(2) (Removes 3rd element)")
    # l1.remove_elel_nth_position(2)
    # l1.display()

    l1.remove_from_end(2)
    l1.display()






