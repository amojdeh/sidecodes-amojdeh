class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num <= 1:
            return False
        
        else:
            
            l = [1]
            
            for i in range(2, int(sqrt(num)) + 1):
                if i == sqrt(num):
                    l.append(sqrt(num))
                    continue
                elif not num%i:
                    l.append(i)
                    l.append(num//i)
        print(l)
        return sum(l) == num
                    