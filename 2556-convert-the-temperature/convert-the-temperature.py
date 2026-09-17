class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        kelvin = 273.15 + celsius
        fahrenhiet = celsius * 1.8 + 32
        ans.append(kelvin)
        ans.append(fahrenhiet)
        
        return ans