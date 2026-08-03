class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse = True)
        
        fleets=0
        prev_time=-1
        for pos, spd in cars:
            curr_time=(target-pos)/spd
            if curr_time>prev_time:
                fleets+=1
                prev_time = curr_time
        return fleets

        