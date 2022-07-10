class Solution:
    def isValid(self, s: str) -> bool:
        dp = []
        getChar = ['(', '{', '[', ')', '}', ']']
        getNum = {
            '(':0, '{':1, '[':2, ')':3, '}':4, ']':5
        }
        for i in s:
            if getNum[i] <= 2:
                dp.append(getNum[i])
            if getNum[i] >= 3:
                if dp and dp[-1] == getNum[i]-3:
                    del dp[-1]
                else:
                    return False
        if dp:
            return False
        else:
            return True