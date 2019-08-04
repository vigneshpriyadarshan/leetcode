from collections import Counter

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        if(len(A)>=4 and len(A)<=10000 and len(A)%2 == 0):
            key_list = list(Counter(A).keys())
            value_list = list(Counter(A).values())
            for i in range(len(value_list)):
                if(i>=0 and i<=10000):
                    if(value_list[i]>1):
                        return key_list[i]
