class Solution:
    def isHappy(self, n: int) -> bool:
        array = []
        s = set(array)
        done = True
        ad = 0
        result = False
        while(done):
            ld = int(n%10)
            n = int(n/10)
            ad = pow(ld,2) + ad
            if(n==0):
                if(ad == 1):
                    result = True
                    done = False
                    break
                if(ad not in s):
                    s.add(ad)
                    n = ad
                    ad = 0
                    done = True
                    continue
                elif(ad in s):
                    done = False
return result
