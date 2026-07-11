class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        for i in range(len(boxes)):
            target= sum(abs(i - j) for j in range(len(boxes)) if boxes[j] == "1")
            result.append(target)
        return result
        