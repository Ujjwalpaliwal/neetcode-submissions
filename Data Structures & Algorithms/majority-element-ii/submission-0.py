class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        ans=[]
        limit = len(nums) // 3   # <-- Ye line missing hai
        for num,count in freq.items():
            if count>limit:
                ans.append(num)
        return ans
        