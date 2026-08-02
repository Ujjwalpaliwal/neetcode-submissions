from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort using Python's built-in efficient sort
        people.sort()
        
        left = 0
        right = len(people) - 1
        boats = 0
        
        while left <= right:
            # Try to pair lightest with heaviest
            if people[left] + people[right] <= limit:
                left += 1  # Light person goes too
                right -= 1 # Heavy person goes
            else:
                right -= 1 # Only heavy person goes alone
            
            boats += 1  # One boat used
        
        return boats