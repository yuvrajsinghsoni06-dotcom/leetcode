# Maximum Ice- Cream Question:

class Solution:
    def totalice_cream(self, costs: list[int],coins : int):
        ice_cream = 0
        n = len(costs)
        costs = sorted(costs)
        if not costs :
            return ice_cream
        for cost in costs:
            if coins >= cost:
                coins -= cost
                ice_cream += 1
        return ice_cream

    
if __name__ == "__main__":
    sol = Solution()
    costs = [1,6,3,1,2,5]
    result = sol.totalice_cream(costs,20)
    print(result)
