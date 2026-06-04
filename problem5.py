# 141. Linked List Cycle  -- to cheack if we are dealing with a circular LinkedList we use Tortiose and Hare Algo : which Instruct us to initialize two pointers, slow and fast. The fast pointer traverses the linked list twice while the slow pointer traverses the linked list once. At that point where the slow and fast pointers meet, it is the point which tells us that the linked list we are dealing with is circular. If not, then it is a single linked list, a linear linked list. 


class Node:
    def __init__(self, value):
        self.value =  value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print("-> ".join(elements) + " -> None")  
    def cycle(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
        






if __name__ == "__main__":
    List1 = LinkedList()
    List1.head = Node(1)
    List1.head.next = Node(2)
    List1.head.next.next = Node(4)
    List1.head.next.next.next = Node(5)

    List1.display()
    # List1.head.next.next.next = List1.head
    print(List1.cycle())