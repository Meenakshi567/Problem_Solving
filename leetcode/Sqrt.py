class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        low, high = 2, x // 2
        ans = 1  
        while low <= high:
            mid = low + (high - low) // 2
            num = mid * mid
            
            if num == x:
                return mid
            elif num < x:
                ans = mid      
                low = mid + 1  
            else:
                high = mid - 1 
                
        return ans
