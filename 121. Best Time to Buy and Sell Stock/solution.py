class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        init = 0
        length = len(prices)
        if(length<=1):
            return 0
        fun = prices[length-1]
        while(fun == 0):
            prices.pop()
            length = len(prices)
            fun = prices[length-1]
        for i in range(0,len(prices)-1):
            array = []
            number = prices[i]
            array = prices[i+1:len(prices)]
            maximum = max(array)
            if(maximum == 0):
                return init
            if(number < prices[i]):
                continue
            else:
                if(maximum - number > init):
                    init = maximum - number
        return init
