# 82. Remove Duplicates from Sorted List II


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

    def duplicacy_ll(self):
        dummy = Node(0)
        dummy.next = self.head
        current = self.head
        prev = dummy
        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                prev.next = current.next

            else:
                prev = prev.next
                
            current = current.next
        return dummy.next

if __name__ == "__main__":
    list = LinkedList()
    list.head = Node(1)
    list.head.next = Node(2)
    list.head.next.next = Node(3)
    list.head.next.next.next = Node(3)
    list.head.next.next.next.next = Node(5)


    list.display()
    print(f"After removing the duplicate values: ->")
    list.duplicacy_ll()
    list.display()