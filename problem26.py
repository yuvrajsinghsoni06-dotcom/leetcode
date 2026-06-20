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

    # Moved directly into LinkedList, removed the extra nested Solution class
    def solution(self, a: int, b: int, list1: Node, list2: Node) -> Node:
        # Step 1: Find the node right BEFORE index 'a'
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next
            
        # Step 2: Find the node right AFTER index 'b'
        post_b = prev_a
        for _ in range(b - a + 2):
            post_b = post_b.next
            
        # Step 3: Find the last node (tail) of list2
        tail_list2 = list2
        while tail_list2.next:  
            tail_list2 = tail_list2.next
            
        # Step 4: Splice list2 in
        prev_a.next = list2       
        tail_list2.next = post_b  
        
        return list1
    

if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(10)                  # Index 0
    llist.head.next = Node(1)             # Index 1
    llist.head.next.next = Node(13)       # Index 2
    llist.head.next.next.next = Node(6)   # Index 3 (Removed)
    llist.head.next.next.next.next = Node(9) # Index 4 (Removed)
    llist.head.next.next.next.next.next = Node(5) # Index 5

    list2 = LinkedList()
    list2.head = Node(4)
    list2.head.next = Node(5)
    list2.head.next.next = Node(9)
    list2.head.next.next.next = Node(14)

    print("Original List 1:")
    llist.display()

    # Call the solution method from llist
    new_head = llist.solution(3, 4, llist.head, list2.head)
    
    # Update llist's head to point to the newly modified list head
    llist.head = new_head
    
    print("\nModified List 1 after splicing:")
    llist.display()