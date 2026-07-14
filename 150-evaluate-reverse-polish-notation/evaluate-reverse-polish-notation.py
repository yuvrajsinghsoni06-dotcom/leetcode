class Solution:
    import operator
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops ={
            "+" : operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }
        for t in tokens:
            result = 0
            if t in ops:
                 b = int(stack.pop())
                 a = int(stack.pop())
                 result = ops[t](a,b)
                 stack.append(result)
            else:
                stack.append(t)

        ans = int(stack[0])
            

            
        return ans


        