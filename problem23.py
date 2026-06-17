

class Node:
    def __init__(self, val):
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
        if not self.head or not self.head.next:
            return self.head
        slow = self.head
        fast = slow.next
        total_sum = 0
        while fast:
            if fast.val != 0:
                total_sum += fast.val
            else:
                slow = slow.next
                slow.val = total_sum
                total_sum = 0

            fast = fast.next
        slow.next = None
        self.head = self.head.next
        return self.head
    
if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(0)
    llist.head.next = Node(3)
    llist.head.next.next = Node(1)
    llist.head.next.next.next = Node(0)
    llist.head.next.next.next.next = Node(4)
    llist.head.next.next.next.next.next = Node(5)
    llist.head.next.next.next.next.next.next = Node(2)
    llist.head.next.next.next.next.next.next.next = Node(0)


    llist.display()
    llist.solution()
    llist.display()


