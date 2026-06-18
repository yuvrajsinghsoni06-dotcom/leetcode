
class Solution:

    def removal(self,stack: list):
        if not stack:
            return None
        return stack.pop()
    def addition(self,stack :list, val : int):
        stack.append(val)
    def display(self, stack:list):
        print(stack)
    

if __name__ == "__main__":
    att = Solution()
    stack = [1,2,3,4,5,6]
    print(att.removal(stack))
    att.display()

    att.addition(stack,11)
    att.display()

