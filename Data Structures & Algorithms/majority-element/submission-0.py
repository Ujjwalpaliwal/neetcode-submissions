class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hasha={}
        for i in nums:
            hasha[i]= hasha.get(i,0)+1
        n= len(nums)
        for key,value in hasha.items():
            if value>n//2:
                return key

        