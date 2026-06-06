class Node:
    def __init__(self, data):
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

    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True

        # Step 1: Find the middle of the linked list
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Step 3: Compare the first half and the reversed second half
        first_half = self.head
        second_half = prev  # 'prev' is now the head of the reversed second half
        
        while second_half:  # We only need to check until the end of the second half
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

if __name__ == "__main__":
    llist = LinkedList()  # Renamed 'list' to 'llist' to avoid built-in conflict
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(2)
    llist.head.next.next.next = Node(1)

    print("Original List:")
    llist.display()

    print(f"Is palindrome? {llist.is_palindrome()}")