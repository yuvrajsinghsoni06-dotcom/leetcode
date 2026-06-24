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

    def solution(self, m: int, n: int):
        # 1. Initialize the matrix filled with -1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        # 2. Define the boundaries
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        current = self.head
        
        # 3. Spiral traversal loop
        while current and top <= bottom and left <= right:
            # Move Right along the top row
            for c in range(left, right + 1):
                if not current: break
                matrix[top][c] = current.val
                current = current.next
            top += 1 # Shrink top boundary
            
            # Move Down along the right column
            for r in range(top, bottom + 1):
                if not current: break
                matrix[r][right] = current.val
                current = current.next
            right -= 1 # Shrink right boundary
            
            # Move Left along the bottom row
            for c in range(right, left - 1, -1):
                if not current: break
                matrix[bottom][c] = current.val
                current = current.next
            bottom -= 1 # Shrink bottom boundary
            
            # Move Up along the left column
            for r in range(bottom, top - 1, -1):
                if not current: break
                matrix[r][left] = current.val
                current = current.next
            left += 1 # Shrink left boundary
            
        return matrix
    
if __name__ == "__main__":
    arr = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
    
    # Instantiate the LinkedList wrapper class
    ll = LinkedList()
    
    # Build the linked list and hook it to ll.head
    ll.head = Node(arr[0])
    current = ll.head
    for i in arr[1:]:
        current.next = Node(i)
        current = current.next
        
    print("Linked List:")
    ll.display()
    
    # Generate a 4x4 matrix from the list
    print("\nSpiral Matrix Result:")
    result_matrix = ll.solution(4, 4)
    for row in result_matrix:
        print(row)