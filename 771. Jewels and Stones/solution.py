class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        if((len(J)<=50 and len(S)<=50) and (Solution().testLetters(J,S))):
            if(Solution().testDistinct(J)):
                for i in range(len(S)):
                    for k in range(len(J)):
                        if(ord(S[i]) == ord(J[k])):
                            count += 1
                            break
            else:
                count = 0
        return count
    def testLetters(self, J: str, S: str) -> bool:
        test = False
        for i in range(len(J)):
            if((ord(J[i])>=65 and ord(J[i])<=90) or (ord(J[i])>=97 and ord(J[i])<=122)):
                test = True
                continue
            else:
                test = False
        for i in range(len(S)):
            if((ord(S[i])>=65 and ord(S[i])<=90) or (ord(S[i])>=97 and ord(S[i])<=122)):
                test = True
                continue
            else:
                test = False
        return test

    def testDistinct(self, st: str) -> bool:
        if len(st) > 256:
            return False
        char_set = [False] * 128
        for i in range(0, len(st)):
            val = ord(st[i])
            if char_set[val]:
                return False
            char_set[val] = True
        return True
