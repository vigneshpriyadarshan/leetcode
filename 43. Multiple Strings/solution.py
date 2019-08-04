class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        value = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        number1 = 0
        number2 = 0
        answer = 0
        if(len(num1)<111 and len(num2)<111 and num1[0]!="0" and num2[0]!="0"):
            negative = True
            for i in num1:
                if(i in value.keys()):
                    number1 = 10 * number1+value[i]
                else:
                    negative = False
                    break
            for j in num2:
                if(j in value.keys()):
                    number2 = 10 * number2+value[j]
                else:
                    negative = False
                    break
            if(negative):
                answer = number1 * number2
        return str(answer) 
