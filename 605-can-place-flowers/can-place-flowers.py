class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
       
        flowerbed.insert(0,2)
        flowerbed.append(2)
        length = len(flowerbed)

        for i in range(1,length - 1):
            if n == 0:
                return True
            if flowerbed[i] == 0 and ( flowerbed[i-1] == 0 or  flowerbed[i-1] == 2) and (flowerbed[i +1] == 0 or  flowerbed[i+1] == 2):
                n -= 1
                flowerbed[i] = 1
        
        return n== 0
            


        