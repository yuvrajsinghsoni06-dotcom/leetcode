class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        for i in range(len(boxes)):
            target= [abs(i - j) for j in range(len(boxes)) if boxes[j] is "1"]
            num = sum(target)

            result.append(num)
        return result
        