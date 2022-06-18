class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        returnLtr = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        answer = []
        def rec(prev, pointer):
            if pointer == len(digits):
                answer.append(prev)
                return
            for i in returnLtr[digits[pointer]]:
                rec(prev+i, pointer+1)
        rec('',0)
        return answer