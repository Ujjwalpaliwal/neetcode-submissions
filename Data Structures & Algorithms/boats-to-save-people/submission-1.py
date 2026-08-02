class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n= len(people)
        for i in range(n):
            for j in range(0,n-i-1):
                if people[j]>people[j+1]:
                    temp=people[j]
                    people[j]=people[j+1]
                    people[j+1]=temp
        left = 0
        right=n-1
        boats=0
        while left<=right:
            if people[left]+people[right]<=limit:
                left =left+1
                right =right -1
            else:
                right =right-1
            boats = boats+1
        return boats
