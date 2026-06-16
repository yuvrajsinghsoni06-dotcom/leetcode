


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


    def llgrecom(self):
        p1 = self.head
        p2 = self.head.next
        grecom = 1
        while p2:
            smaller = p1.val if p1.val < p2.val else p2.val
            for i in range(1, smaller+1):
                if (p1.val % i == 0) and (p2.val % i == 0):
                    grecom = i
            hcf = Node(grecom)
            p1.next = hcf
            hcf.next = p2
            p1 = p2
            p2 = p2.next

        return self.head


        
            




if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(18)
    llist.head.next = Node(6)
    llist.head.next.next  = Node(10)
    llist.head.next.next.next = Node(3)
    # llist.head.next.next.next.next = Node(5)


    llist.display()

    llist.llgrecom()
    llist.display()
    