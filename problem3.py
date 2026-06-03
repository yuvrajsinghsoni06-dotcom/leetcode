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

    def merge_sorted_list(self, list1, list2):
        dummy = Node(0)
        current = dummy
        
        # Track active pointers without destroying the original lists' heads
        p1, p2 = list1.head, list2.head
        
        while p1 and p2:
            if p1.data < p2.data:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
            
        # Clean up: Attach the remaining non-empty list segment
        current.next = p1 if p1 else p2
        
        self.head = dummy.next
        return self.head
    

if __name__ == "__main__":
    list1 = LinkedList()
    list1.head = Node(1)
    list1.head.next = Node(3)
    list1.head.next.next = Node(89)
    list2 = LinkedList()
    list2.head = Node(1)
    list2.head.next = Node(6)
    list2.head.next.next = Node(9)


    print("list1")
    list1.display()
    print("list2")
    list2.display()
    
    merge_list = LinkedList()
    merge_list.merge_sorted_list(list1,list2)
    print("Merged List")
    merge_list.display()



