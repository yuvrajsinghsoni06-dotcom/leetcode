class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.val))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def to_array(self):
        # Step 1: Convert the linked list to a standard Python list
        values = []
        current = self.head
        while current:
            values.append(current.val)
            current = current.next
        
        # Step 2: Initialize the answer array with 0s
        answer = [0] * len(values)
        stack = []  # This will store indices
        
        # Step 3: Use a monotonic stack to find next greater elements
        for i in range(len(values)):
            # While stack is not empty and current value is greater than 
            # the value at the index stored at the top of the stack
            while stack and values[i] > values[stack[-1]]:
                index_to_update = stack.pop()
                answer[index_to_update] = values[i]
            
            # Push the current index onto the stack
            stack.append(i)
            
        return answer


if __name__ == "__main__":
    # Test Case 1: [1, 2, 3, 4] -> Expected output: [2, 3, 4, 0]
    list1 = LinkedList()
    list1.head = Node(1)
    list1.head.next = Node(2)
    list1.head.next.next = Node(3)
    list1.head.next.next.next = Node(4)
    
    print("List 1:")
    list1.display()
    print("Next Greater Elements:", list1.to_array())
    print("-" * 30)

    # Test Case 2: [2, 7, 4, 3, 5] -> Expected output: [7, 0, 5, 5, 0]
    list2 = LinkedList()
    list2.head = Node(2)
    list2.head.next = Node(7)
    list2.head.next.next = Node(4)
    list2.head.next.next.next = Node(3)
    list2.head.next.next.next.next = Node(5)
    
    print("List 2:")
    list2.display()
    print("Next Greater Elements:", list2.to_array())