class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            if n == 1:
                return True
        if n == 0:
            return True
        if len(flowerbed) > 1 and flowerbed[0] == flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
            if n <= 0:
                return True

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n <= 0:
                    return True
        if len(flowerbed) > 1 and flowerbed[-1] == flowerbed[-2] == 0:
            n -= 1
            if n <= 0:
                return True
        return False
