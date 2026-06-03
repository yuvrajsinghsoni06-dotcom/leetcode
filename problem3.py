# Merge two sorted linkedlist into one large sorted LinkedList:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ->')
            current = current.next
        print("None")

    def merge_sorted_list(self, list1 , list2):
        dummy = Node(0)
        current = dummy
        while list1.head is not None and list2.head is not None:
            if list1.head.data < list2.head.data:
                current.next = list1.head
                list1.head = list1.head.next
            else:
                current.next = list2.head
                list2.head = list2.head.next

            current = current.next
            
        if list1.head is not None:
            current.next = list1.head
        elif list2.head is not None:
            current.next = list2.head
            
        self.head = dummy.next
        return self.head


                
        





if __name__ == "__main__":
    list1 = LinkedList()
    list1.head = Node(1)
    list1.head.next = Node(2)
    list1.head.next.next = Node(3)

    list2 = LinkedList()
    list2.head = Node(1)
    list2.head.next = Node(3)
    list2.head.next.next = Node(4)


    list1.display()
    list2.display()

    merged_list = LinkedList()
    merged_list.merge_sorted_list(list1,list2)
    merged_list.display()