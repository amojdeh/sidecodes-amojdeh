class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        first = 0
        second = 0
        
        for i in range(len(num1)):
            
            first += (int(num1[i])*10**(len(num1)-(i+1)))
            
        for i in range(len(num2)):
            
            second += (int(num2[i])*10**(len(num2)-(i+1)))
            
        return str(first + second)