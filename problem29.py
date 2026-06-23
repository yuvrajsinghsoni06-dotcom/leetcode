


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
        total = 0
        current = self.head
        while current:
            total = current.val  + (total * 2)
            current = current.next
        return total


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(0)
    llist.head.next.next = Node(1)

    llist.display()
    result = llist.solution()
    print(result)
