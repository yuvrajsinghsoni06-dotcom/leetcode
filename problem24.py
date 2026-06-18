
class Solution:

    def removal(self,stack: list):
        if stack is None:
            return stack
        stack.pop()
        return stack
    def addition(self,stack :list, val : int):
        stack.append(val)
        return stack
    

if __name__ == "__main__":
    att = Solution()
    stack = [1,2,3,4,5,6]
    print(att.removal(stack))
    print(att.addition(stack,11))

