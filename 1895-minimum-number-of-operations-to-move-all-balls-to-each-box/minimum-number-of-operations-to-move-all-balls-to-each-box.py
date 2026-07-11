class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        
        # Pass 1: Left to Right
        balls = 0
        ops = 0
        for i in range(n):
            result[i] += ops
            if boxes[i] == "1":
                balls += 1
            ops += balls  # Each ball carried takes 1 step to move to the next box
            
        # Pass 2: Right to Left
        balls = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            result[i] += ops
            if boxes[i] == "1":
                balls += 1
            ops += balls
            
        return result