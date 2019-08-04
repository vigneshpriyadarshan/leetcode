class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        upper = ['q','w','e','r','t','y','u','i','o','p']
        middle = ['a','s','d','f','g','h','j','k','l']
        lower = ['z','x','c','v','b','n','m']
        result_list = []
        for i in range(len(words)):
            word_length = len(words[i])
            iterate = 0
            upper_count = 0
            middle_count = 0
            lower_count = 0
            for j in words[i]:
                if j.lower() in upper:
                    upper_count += 1
                if j.lower() in middle:
                    middle_count += 1
                if j.lower() in lower:
                    lower_count += 1
            if(word_length == upper_count or word_length == middle_count or word_length == lower_count):
                result_list.append(words[i])
        return result_list
