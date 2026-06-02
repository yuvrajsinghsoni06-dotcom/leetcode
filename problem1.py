class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def add_two_linked_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    # Use standard pointers to traverse so we don't destroy the original lists
    p1 = l1.head
    p2 = l2.head
    
    # Create a dummy head to easily build the new result list
    dummy_head = Node(0)
    current = dummy_head
    carry = 0
    
    while p1 or p2 or carry:
        val1 = p1.value if p1 else 0
        val2 = p2.value if p2 else 0
        
        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        # Create new node and move result pointer
        current.next = Node(digit)
        current = current.next
        
        # Advance input pointers safely
        if p1: p1 = p1.next
        if p2: p2 = p2.next
            
    result_list = LinkedList()
    result_list.head = dummy_head.next
    return result_list

# --- Execution ---

# Create independent List 1: 1 -> 2 -> 3
list1 = LinkedList()
list1.head = Node(2)
list1.head.next = Node(3)
list1.head.next.next = Node(4)

# Create independent List 2: 1 -> 2 -> 3
list2 = LinkedList()
list2.head = Node(3)
list2.head.next = Node(7)
list2.head.next.next = Node(9)

print("List 1:")
list1.display()
print("List 2:")
list2.display()

print("\nResult of addition:")
result = add_two_linked_lists(list1, list2)
result.display()