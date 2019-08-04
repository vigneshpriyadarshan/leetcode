class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums,first,last,target):
            if last >= first:
                mid = int(first + (last-first) / 2)
                if(nums[mid]==target):
                    return mid
                elif(target>nums[mid]):
                    return binarySearch(nums,mid+1,last,target)
                else:
                    return binarySearch(nums,first,mid-1,target)
            else:
                return -1
        index = binarySearch(nums,0,len(nums)-1,target)
        if index!=-1:
            return index
        else:
            return -1
