

class Node:
    def __init__(self,val):
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
        print(" -> ".join(element) + " -> None ")


    def max_twin_sum(self):
        slow = self.head
        fast = self.head
        t_sum = 0
        while fast:
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        first_head = self.head
        sec_head = prev
        while sec_head:
            sum = first_head.val + sec_head.val
            if t_sum < sum:
                t_sum = sum
            first_head = first_head.next
            sec_head = sec_head.next
        return t_sum
    


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(4)
    llist.head.next = Node(2)
    llist.head.next.next = Node(2)
    llist.head.next.next.next = Node(3)

    llist.display()


    print(llist.max_twin_sum())




        
