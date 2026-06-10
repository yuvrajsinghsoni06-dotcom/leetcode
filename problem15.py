# 237. Delete Node in a Linked List

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

    def deletion_of_node(self,node):
        node.val = node.next.val
        node.next = node.next.next
        return self.head
    

if __name__ == "__main__":
    list = LinkedList()
    deletion_node = Node(2)


    list.head = Node(1)
    list.head.next = deletion_node
    
    list.head.next.next = Node(3)
    list.head.next.next.next = Node(4)
    list.head.next.next.next.next = Node(5)


    list.display()
    list.deletion_of_node(deletion_node)
    list.display()
