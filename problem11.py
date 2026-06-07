
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

    def swap(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        self.head = dummy.next
        



if __name__ == "__main__":
    list = LinkedList()
    list.head = Node(5)
    list.head.next = Node(2)
    list.head.next.next = Node(3)
    list.head.next.next.next = Node(1)

    list.display()
    list.swap()
    list.display()