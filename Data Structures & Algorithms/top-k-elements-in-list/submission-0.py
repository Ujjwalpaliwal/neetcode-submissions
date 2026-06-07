class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashb={}
        for num in nums:
            hashb[num]= hashb.get(num,0)+1
        sorted_items = sorted(hashb.items(),
        key=lambda x:x[1],
        reverse=True
        )
        result=[]
        for i in range(k):
            result.append(sorted_items[i][0])
        return result

        