class Solution:
    def romanToInt(self, s: str) -> int:
        if not len(s):
            return 0
        symbToVal = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        prev = s[0]
        save_val = symbToVal[prev]
        answer = 0
        for i in range(1, len(s)):
            current = s[i]
            if symbToVal[prev] == symbToVal[current]:
                save_val += symbToVal[current]
            else:
                if symbToVal[prev] > symbToVal[current]:
                    answer +=  + save_val
                    save_val = symbToVal[current]
                elif symbToVal[prev] < symbToVal[current]:
                    answer += symbToVal[current] - save_val
                    save_val = 0
            prev = current
        answer += save_val
        return answer