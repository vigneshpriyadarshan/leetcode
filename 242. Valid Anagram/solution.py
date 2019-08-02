from collections import Counter as count
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        summation = 0
        s1 = sorted(s)
        t1 = sorted(t)
        if(len(s1)!=len(t1)):
            return False
        for i in range(len(s1)):
            if(s1[i]==t1[i]):
                summation = summation + 1
        if(summation == len(s1)):
            return True
        else:
            return False
