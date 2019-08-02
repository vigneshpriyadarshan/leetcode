class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minimum = 0
        answer = []
        if(len(list1)<1000 and len(list2)<1000):
            for i in range(0,len(list1)):
                if(list1[i] in list2):
                    number = list2.index(list1[i]) + i
                    if(minimum == 0):
                        if(i == 0):
                            minimum = number
                            answer.append(list1[i])
                        elif(i>0 and len(answer)==0):
                            minimum = number
                            answer.clear()
                            answer.append(list1[i])
                    elif(i>0 and number < minimum):
                        minimum = number
                        answer.clear()
                        answer.append(list1[i])
                    elif(i>0 and number == minimum):
                        minimum = number
                        answer.append(list1[i])
        return answer






