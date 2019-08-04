class Solution(object):
    def addDigits(self, num):
        return num if num == 0 else num % 9 or 9
