class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        for i in range(len(boxes)):
            target = []
            for j in range(len(boxes)):
                if boxes[j] is "1":
                    num = abs(i - j)
                    target.append(num)
            result.append(sum(target))
        return result

        
                


        