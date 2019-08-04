class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        dec = K
        result = 0
        if(len(A)>=1 and len(A)<=10000 and dec>=1 and K<=10000):
            while(dec):
                minValue = min(A)
                if(minValue>100 or minValue<-100):
                    return result
                    break
                else:
                    index = A.index(minValue)
                    replace = 0 - minValue
                    A[index] = replace
                    dec = dec - 1
            result = sum(A)
        return result
