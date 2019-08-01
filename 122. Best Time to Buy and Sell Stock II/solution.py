class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        if(len(prices)<=1):
            return 0
        num = prices[len(prices)-1]
        if(num == 0):
            prices.pop()
            num = prices[len(prices)-1]
        localMin = prices[0]
        for i in range(1,len(prices)-1):
            if(localMin<prices[i] and (i==len(prices)-1)):
                return 0
            if(localMin<prices[i]):
                break
            else:
                localMin = prices[i]
        profit = localMin
        ind = prices.index(localMin)
        for i in range(ind,len(prices)-1):
            localMax = prices[i+1]
            if(localMin < localMax and (i+1==len(prices)-1)):
                result = result + (localMax-profit)
                break
            if(localMin < localMax):
                localMin = prices[i+1]
                continue
            if(localMin >= localMax):
                result = result + (localMin - profit)
                localMin = prices[i+1]
                profit = localMin
        return result




        
