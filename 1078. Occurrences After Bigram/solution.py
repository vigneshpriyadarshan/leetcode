class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        answer = []
        text = text.split(" ")
        for i in range(0,len(text)-2):
            if(text[i] == first and text[i+1] == second):
                answer.append(text[i+2])
        return answer        
