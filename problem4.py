# to removbe duplicay data from sorted linkedlist:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def remove_duplicacy(self, list1):
        # Handle edge case: empty list or single-node list
        if not list1.head:
            return None
        
        current = list1.head
        
        # Traverse until the second to last node
        while current and current.next:
            if current.data == current.next.data:
                # 🟢 Skip the duplicate node by pointing past it
                current.next = current.next.next
            else:
                # 🟢 Only move forward if no duplicate was found
                current = current.next
                
        self.head = list1.head
        return self.head
    
if __name__ == "__main__":
    list1 = LinkedList()
    list1.head = Node(1)
    list1.head.next = Node(1)
    list1.head.next.next = Node(2)
    list1.head.next.next.next = Node(2)
    list1.head.next.next.next.next = Node(3)
    list1.head.next.next.next.next.next = Node(3)
    list1.head.next.next.next.next.next.next = Node(4)

    print("Orginal LinkedList: ")
    list1.display()

    rem_dup = LinkedList()
    rem_dup.remove_duplicacy(list1)
    print("LinkedList after removing duplicates: ")
    rem_dup.display()