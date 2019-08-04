class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = []
        result.insert(0,0)
        for i in range(1,amount+1):
            result.insert(i,99999999)
        for i in range(len(coins)):
            for j in range(1,len(result)):
                if(j>=coins[i]):
                    result[j] = min(result[j],1+result[j-coins[i]])
        final = result.pop()
        if(final == 99999999):
            return -1
        else:
            return final
