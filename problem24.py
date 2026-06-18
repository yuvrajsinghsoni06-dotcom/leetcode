class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # Pop the top element if stack isn't empty, otherwise use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for the closing bracket doesn't match the popped element
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets found their match
        return not stack

# --- Testing the code ---
if __name__ == "__main__":
    sol = Solution()
    
    test1 = "()[]{}"
    test2 = "(]"
    test3 = "([)]"
    
    print(f"Is '{test1}' valid?: {sol.isValid(test1)}")  # Expected: True
    print(f"Is '{test2}' valid?: {sol.isValid(test2)}")  # Expected: False
    print(f"Is '{test3}' valid?: {sol.isValid(test3)}")  # Expected: False