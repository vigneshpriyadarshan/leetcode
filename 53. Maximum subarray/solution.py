class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return -2147483648
        elif(len(nums)==1):
            return nums[0]
        summ = 0
        result = 0
        count = 0
        for i in range(0,len(nums)):
            if(nums[i]<0):
                count = count + 1
            summ = summ + nums[i]
            if(result<summ):
                result = summ
            if(summ<0):
                summ = 0
        if(count == len(nums)):
            return max(nums)
        return result        
