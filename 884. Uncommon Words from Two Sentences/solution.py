from collections import Counter as c
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        result = []
        if(len(A)>=0 and len(A)<=200 and len(B)>=0 and len(B)<=200):
            spaceA = A.split(" ")
            spaceB = B.split(" ")
            copySpaceA = spaceA
            for key,val in c(spaceA).items():
                if(val == 1 and key not in spaceB):
                    result.append(key)
            for key,val in c(spaceB).items():
                if(val == 1 and key not in copySpaceA):
                    result.append(key)
        return result  
