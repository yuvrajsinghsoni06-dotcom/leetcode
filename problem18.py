# sort the list in ascending order:-

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
        print(" -> ".join(element) + " -> None")


    def sorting_list(self):
        current = self.head
        arr = []
        while current:
            arr.append(int(current.data))
            current = current.next
        arr.sort()

        cur = self.head
        for val in arr:
            cur.data = val
            cur = cur.next

        return self.head
    
if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(4)
    llist.head.next = Node(2)
    llist.head.next.next = Node(1)
    llist.head.next.next.next = Node(3)

    llist.display()

    llist.sorting_list()
    llist.display()