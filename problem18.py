""" sort the list in ascending order:- method -1 we can just like converting - Link list into an array, then sort it using the built-in sort method, then again rebuild the link list from it.
It will give a time complexity of + O(log n), which will be an optimal time complexity, but as we are storing the data using an array, we will get a space complexity of O(n)."""

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