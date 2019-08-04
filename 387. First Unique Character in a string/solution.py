from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if(len(s) == 0):
            return -1
        count = Counter(s)
        length = len(s)
        flag = 0
        for i in s:
            if(count.get(i,'') == 1):
                return s.find(i)
            else:
                flag += 1
        if(length == flag):
            return -1
