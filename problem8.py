 # 206. Reverse Linked List - In a linked list, we have to reverse the order of the nodes we are given. Suppose we are given 1, 2, 3, 4, 5. Now the read code wants us to represent our node as 5, 4, 3, 2, 1, None. 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def display(self):
        current = self.head
        element = []
        while current:
            element.append(str(current.data))
            current = current.next
        print("-> ".join(element) + "-> None")

    def reverselist(self):
        pre = None
        current = self.head
        while current:
            next_node = current.next
            current.next = pre
            pre = current
            current = next_node

        self.head = pre
        return self.head
        
if __name__ == "__main__":
    list = LinkedList()
    list.head = Node(1)
    list.head.next = Node(2)
    list.head.next.next = Node(3)
    list.head.next.next.next = Node(4)
    list.head.next.next.next.next = Node(5)

    list.display()
    print(f"After reversing the order:")
    list.reverselist()
    list.display()