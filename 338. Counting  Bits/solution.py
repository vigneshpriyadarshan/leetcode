class Solution:
    def countBits(self, num: int) -> List[int]:
        result_list = []
        for i in range(num+1):
            result_list.append(Solution().binaryCount(i))
        return result_list

    def binaryCount(self, n):
        count = 0
        while(n):
            n = n & (n-1)
            count += 1
        return count
            
