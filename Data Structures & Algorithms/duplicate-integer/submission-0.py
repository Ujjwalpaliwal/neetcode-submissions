class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        me=set()
        for i in nums:
            if i in me:
                return True
            me.add(i)
        return False