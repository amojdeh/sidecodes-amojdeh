class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n == 1 or n == 0
        
        
        for i in range(len(flowerbed)):
            
            if flowerbed[i] == 0:
                
                if i != 0 and i != len(flowerbed) - 1:
                    left = flowerbed[i-1]
                    right = flowerbed[i+1]
                    
                    if right == 0 and left == 0:
                        count += 1
                        flowerbed[i] = 1
                elif i == 0:
                    if flowerbed[1] == 0:
                        count += 1
                        flowerbed[0] = 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[-2] == 0:
                        count += 1
                        flowerbed[-1] = 1
        return count >= n