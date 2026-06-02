class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.value, end= " -> ")
            current = current.next
        print("None")

obj = Node(1)
obj.next = Node(2)
obj.next.next = Node(3)

l1 = LinkedList()
l1.head = obj
l1.display()

l2 = LinkedList()
l2.head = obj
l2.display()
rem = 0
while l1.head is not None or l2.head is not None:
    if l1.head:
        value1 = l1.head.value
        l1.head = l1.head.next
    else:
        value1 = 0
    if l2.head:
        value2 = l2.head.value
        l2.head = l2.head.next
    else: 
        value2 = 0
    
    total = value1 + value2 + rem
    rem = total // 10
    digit = total % 10
    print(digit, end= " -> ")
print("None")