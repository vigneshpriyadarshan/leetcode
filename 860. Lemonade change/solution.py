class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        collect = []
        result = 0
        for i in range(0,3):
            collect.append(0)
        if(len(bills)>0 and len(bills)<=10000):
            if bills[0]!=5:
                return False
            else:
                collect[0] = collect[0] + 1
                for i in range(1,len(bills)):
                    if(bills[i]==5):
                        collect[0] = collect[0] + 1
                        continue
                    if(bills[i]==10):
                        if(collect[0]>=1):
                            collect[0] = collect[0] - 1
                            collect[1] = collect[1] + 1
                            continue
                        else:
                            result = -1
                            break
                    if(bills[i]==20):
                        if(collect[1]>=1 and collect[0]>=1):
                            collect[1] = collect[1] - 1
                            collect[0] = collect[0] - 1
                            collect[2] = collect[2] + 1
                            continue
                        elif(collect[0]>=3):
                            collect[0] = collect[0] - 3
                            collect[2] = collect[2] + 1
                            continue
                        else:
                            result = -1
                            break
                    else:
                        result = -1
                        break
            if(result<0):
                return False
            else:
                return True
