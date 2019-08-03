class Solution:
    def integerBreak(self, n: int) -> int:
        array = []
        count = 1
        if(n==4):
            array.append(n)
        elif(n==3):
            array.append(2)
        elif(n==2):
            array.append(1)
        while(n>1):
            num = n-3
            array.append(num*pow(3,count))
            count += 1
            n = num
        return max(array)
