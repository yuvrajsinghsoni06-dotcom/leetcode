# 876. Middle of the Link

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

    def middlenode(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle_node = slow.data
        return middle_node


if __name__ == "__main__":
    list = LinkedList()
    list.head = Node(1)
    list.head.next = Node(2)
    list.head.next.next = Node(3)
    list.head.next.next.next = Node(4)
    list.head.next.next.next.next = Node(5)

    list.display()
    print(f"Middle Node of a Singly Linked List :")
    a = list.middlenode()
    print(a)