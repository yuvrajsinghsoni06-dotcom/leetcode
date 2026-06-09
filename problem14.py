class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self, limit=10):
        """Prints the list up to a limit to prevent infinite loops if a cycle exists."""
        current = self.head
        element = []
        count = 0
        while current and count < limit:
            element.append(str(current.val))
            current = current.next
            count += 1
        
        if current:
            element.append("... (Cycle Connected)")
        else:
            element.append("None")
        print(" -> ".join(element))

    def cycle(self, pos):
        """Creates a cycle linking the tail node to the node at index 'pos'."""
        if pos < 0 or not self.head:
            return
        
        change_node = None
        current = self.head
        tail = self.head
        index = 0
        
        # Traverse to find the exact last node (tail)
        while tail.next:
            if index == pos:
                change_node = current
            tail = tail.next
            current = current.next
            index += 1
            
        # Catch condition if pos is the absolute last node index
        if index == pos:
            change_node = current
            
        # Connect the tail's next reference back to the change node
        if change_node:
            tail.next = change_node

    def detectCycle(self):
        """
        LeetCode 142 Solution: Floyd's Tortoise and Hare
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not self.head or not self.head.next:
            return None

        slow = self.head
        fast = self.head
        
        # Phase 1: Determine if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # Executes only if the while loop finishes normally (meaning fast reached None)
            return None
        
        # Phase 2: Find the exact start of the cycle.
        # Reset fast back to head, move both pointers at 1x speed.
        fast = self.head
        while fast != slow:
            fast = fast.next
            slow = slow.next
            
        return fast  # Both pointers meet exactly at the cycle entrance node

# --- Execution Test Block ---
if __name__ == "__main__":
    # 1. Initialize the Linked List
    list1 = LinkedList()
    list1.head = Node(1)
    list1.head.next = Node(2)
    list1.head.next.next = Node(3)
    list1.head.next.next.next = Node(4)

    print("Original List Structure:")
    list1.display()

    # 2. Inject a cycle at index 1 (Node value 2)
    list1.cycle(1)
    print("\nList Structure After Injecting Cycle:")
    list1.display()
    
    # 3. Execute the detection algorithm
    cycle_start_node = list1.detectCycle()
    
    print("\n--- Detection Verdict ---")
    if cycle_start_node:
        print(f"Success! Cycle detected starting at Node with value: {cycle_start_node.val}")
    else:
        print("No cycle detected in this linked list.")