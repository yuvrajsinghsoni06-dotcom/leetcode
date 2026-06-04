# 160. Intersection of Two Linked Lists

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.val))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def intersection(self,p1 , p2):
        p1 = list.head
        p2 = list1.head
        while p1 is not p2:
            p1 = p1.next if p1 else p2
            p2 = p2.next if p2 else p1
        return p1.val if p1 else None
    




if __name__ == "__main__":
    list = LinkedList()
    list.head = Node(1)
    list.head.next = Node(2)
    list.head.next.next = Node(4)
    list.head.next.next.next = Node(5)



    list1 = LinkedList()
    list1.head = Node(8)
    list1.head.next = Node(9)
    list1.head.next.next = Node(3)
    list1.head.next.next.next = Node(7)



    list2 = LinkedList()
    list2.head = Node(10)
    list2.head.next = Node(9)
    list2.head.next.next = Node(3)
    list2.head.next.next.next = Node(7)

    list.display()
    list1.display()
    list2.display()


    list.head.next.next.next = list2.head
    list1.head.next.next.next = list2.head
    list2.intersection(list.head, list1.head)
    print(list2.intersection(list.head, list1.head))





    