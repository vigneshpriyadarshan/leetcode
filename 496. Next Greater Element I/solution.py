class Solution:
    def nextGreaterElement(self, nums1, nums2):
        answer = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if(nums1[i] == nums2[j]):
                    k = j + 1
                    value = False
                    store = 0
                    while(k<len(nums2)):
                        if(nums2[k] > nums1[i]):
                            value = True
                            store = nums2[k]
                            break
                        else:
                            k += 1
                            value = False
                            continue
                    if(value is False):
                        answer.append(-1)
                        break
                    else:
                        answer.append(store)
                        break
        return answer
