class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(0,len(nums)):
            temp = a
            a = max(nums[i]+b,a)
            b = temp
        return a    
