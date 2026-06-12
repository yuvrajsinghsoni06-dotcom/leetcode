class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: 0 or 1 node is already sorted
        if not head or not head.next:
            return head
        
        # Step 1: Find middle and split
        mid = self.getMid(head)
        right = mid.next
        mid.next = None          # cut the list into two halves
        
        # Step 2: Recursively sort both halves
        left  = self.sortList(head)
        right = self.sortList(right)
        
        # Step 3: Merge sorted halves
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head
        # Using fast.next and fast.next.next finds the left-middle node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow          # slow is at the midpoint
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2   # attach remaining nodes
        return dummy.next

# Helper function to display the linked list given its head node
def display(head):
    current = head
    element = []
    while current:
        element.append(str(current.val))
        current = current.next
    print(" -> ".join(element) + " -> None")

    
if __name__ == "__main__":
    # 1. Construct the manual linked list: 4 -> 2 -> 1 -> 3 -> None
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    print("Original List:")
    display(head)

    # 2. Instantiate the solution and sort the list
    sorter = Solution()
    sorted_head = sorter.sortList(head)

    print("\nSorted List:")
    display(sorted_head)