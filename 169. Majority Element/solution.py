class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if(count == 0):
                candidate = nums[i]
                count += 1
            else:
                if(candidate == nums[i]):
                    count += 1
                else:
                    count = count - 1
        count = 0
        for i in range(len(nums)):
            if(candidate == nums[i]):
                count += 1
        if(count > len(nums)/2):
            return candidate
