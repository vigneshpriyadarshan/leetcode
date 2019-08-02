class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        copynum1 = list(set(nums1))
        copynum2 = list(set(nums2))
        maximum = 0
        if(len(copynum1) > len(copynum2)):
            maximum = len(copynum1)
            for i in range(0,maximum):
                if(copynum1[i] in copynum2):
                    res.append(copynum1[i])
        else:
            for i in range(0,len(copynum2)):
                if(copynum2[i] in copynum1):
                    res.append(copynum2[i])
        return res
