


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
        print(" -> ".join(element) + " -> None")

    def solution(self):
        if not self.head or  not self.head.next:
            return self.head
        even = self.head.next
        odd = self.head
        evenhead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return self.head


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(3)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(5)
    llist.head.next.next.next.next.next = Node(6)


    llist.display()
    llist.solution()
    llist.display()
    