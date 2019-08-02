class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sortS = sorted(s)
        sortT = sorted(t)
        res = None
        for i in range(0,len(sortT)-1):
            if(sortS[i] != sortT[i]):
                res = sortT[i]
                break
            else:
                continue
        if(res is None and len(sortT)>len(sortS)):
            res = sortT[len(sortT)-1]
            return res
        elif(res is not None):
            return res
