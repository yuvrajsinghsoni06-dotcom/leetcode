# 92. Reverse Linked List II

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        element = []
        while current:
            element.append(str(current.val))
            current = current.next

        print("-> ".join(element) + "-> None")


    def reversing_a_list(self, left: int , right:int):
        if not self.head or left == right:
            return self.head
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for i in range(left-1):
            prev = prev.next
        current = prev.next

        
        for _ in range(right - left):
           next_node = current.next
           current.next = next_node.next
           next_node.next = prev.next
           prev.next = next_node

        return dummy.next


        
            
        



if __name__ == "__main__":
    list1 = LinkedList()
    list1.head = Node(1)
    list1.head.next = Node(2)
    list1.head.next.next = Node(3)
    list1.head.next.next.next = Node(4)
    list1.head.next.next.next.next = Node(5)

    list1.display()

    print("After swaping left amd right")
    list1.reversing_a_list(2,4)
    list1.display()
