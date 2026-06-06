# 876. Middle of the Link

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

    def middlenode(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


if __name__ == "__main__":
    llist = LinkedList()  # Renamed 'list' to 'llist' to avoid built-in conflicts
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(3)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(5)

    print("Original Full List:")
    llist.display()

    print("\nFinding the middle...")
    mid_node = llist.middlenode()  # Capture the returned node (Node 3)

    # Temporary update to head so 'display()' prints from the middle onward
    llist.head = mid_node 
    
    print("List from Middle to Last Node:")
    llist.display()