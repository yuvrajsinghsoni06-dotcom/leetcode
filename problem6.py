class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self) -> None:
        current = self.head
        elements = []
        while current:
            elements.append(str(current.val))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def intersection(self, headA: Node | None, headB: Node | None) -> int | None:
        # If either list is empty, there can be no intersection
        if not headA or not headB:
            return None
            
        p1 = headA
        p2 = headB
        
        while p1 is not p2:
            # If p1 reaches the end, swap it to the head of List B; else move next
            p1 = p1.next if p1 else headB
            # If p2 reaches the end, swap it to the head of List A; else move next
            p2 = p2.next if p2 else headA
            
        # If they match, return the value (or Node depending on LeetCode requirements)
        return p1.val if p1 else None


if __name__ == "__main__":
    # 1. Create the unique starting chain for List A: 1 -> 2 -> 4
    listA = LinkedList()
    listA.head = Node(1)
    listA.head.next = Node(2)
    listA.head.next.next = Node(4)

    # 2. Create the unique starting chain for List B: 8 -> 9 -> 3
    listB = LinkedList()
    listB.head = Node(8)
    listB.head.next = Node(9)
    listB.head.next.next = Node(3)

    # 3. Create the shared intersecting section: 10 -> 9 -> 3 -> 7 -> None
    shared_list = LinkedList()
    shared_list.head = Node(10)
    shared_list.head.next = Node(9)
    shared_list.head.next.next = Node(3)
    shared_list.head.next.next.next = Node(7)

    # 4. Attach the end of List A and List B to point to the shared list head
    listA.head.next.next.next = shared_list.head   # 4 -> 10
    listB.head.next.next.next = shared_list.head   # 3 -> 10

    # Display the final structures
    print("List A path:")
    listA.display()
    print("List B path:")
    listB.display()

    # Find intersection point
    engine = LinkedList()
    result = engine.intersection(listA.head, listB.head)
    print(f"\nIntersection found at node value: {result}")