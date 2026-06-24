

# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def display(self):
#         current = self.head
#         element = []
#         while current:
#             element.append(str(current.val))
#             current =current.next
#         print(" -> ".join(element) + " -> None ")

#     def solution(self,m : int , n : int):
#         a = m * n
#         arr = []
#         while a < 0:
#             arr.append(-1)
#             a -= 


def solution(m,n):
    matrix = [[-1 for i in range(n)]for i in range(m)]

    return matrix

a  =solution(3,5)
print(a)
    



