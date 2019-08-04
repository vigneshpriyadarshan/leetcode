class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if(n<=1690):
            array = []
            array.append(1)
            identify_two = 0
            identify_three = 0
            identify_five = 0
            for i in range(1,n):
                num = min(array[identify_two]*2,array[identify_three]*3,array[identify_five]*5)
                array.insert(i,num)
                if num%2 == 0:
                    identify_two += 1
                if num%3 == 0:
                    identify_three += 1
                if num%5 == 0:
                    identify_five += 1
            return array[n-1]
