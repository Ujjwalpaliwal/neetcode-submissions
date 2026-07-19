class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 0, x
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Use division to avoid overflow
            if mid == x // mid:
                return mid
            elif mid < x // mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return right