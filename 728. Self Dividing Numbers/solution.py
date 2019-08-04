class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        if(1<=left<=right<=10000):
            result = []
            def checkSelfDiv(num):
                i = num
                done = False
                if(num%10 != 0):
                    while(num>=1):
                        rem = num % 10
                        if(rem != 0):
                            if(i % rem == 0):
                                num = int(num/10)
                                done = True
                            else:
                                done = False
                                break
                        else:
                            done = False
                            break
                return done
            for i in range(left,right+1):
                num = False
                if(i>=1 and i<=9):
                    result.append(i)
                else:
                    num = checkSelfDiv(i)
                if(num == True):
                    result.append(i)
            return result
