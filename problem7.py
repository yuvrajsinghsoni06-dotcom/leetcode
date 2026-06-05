#  203. Remove Linked List Elements - in which We are given a linked list with an integer value val. If a linked list node value is equal to the given val value, then we have to remove that node and update our linked list and return  our linked list such that it does not contain any value which is equal to val. 

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

    def removeElements(self, val):
        dummy = Node(0)
        current = dummy
        current.next = self.head
        while current and current.next:
            if current.next.data == val:
                current.next = current.next.next
            else:
                current = current.next
                 
        self.head = dummy.next
        return self.head



if __name__ == "__main__":
    list =LinkedList()
    list.head = Node(1)
    list.head.next = Node(2)
    list.head.next.next = Node(6)
    list.head.next.next.next = Node(3)
    list.head.next.next.next.next = Node(4)
    list.head.next.next.next.next.next = Node(5)
    list.head.next.next.next.next.next.next = Node(6)

    list1 =LinkedList()
    list1.head = Node(7)
    list1.head.next = Node(7)
    list1.head.next.next = Node(7)
    list1.head.next.next.next = Node(7)
    list1.head.next.next.next.next = Node(7)
    list1.head.next.next.next.next.next = Node(7)
    list1.head.next.next.next.next.next.next = Node(1)

    list.display()
    print("After removing value 6:")
    list.removeElements(6)
    list.display()

    list1.display()
    print("List1 after removing val 7:")
    list1.removeElements(7)
    list1.display()
