class Solution:
    def intToRoman(self, num: int) -> str:
        num_table = [[],
                     [0],
                     [0, 0],
                     [0, 0, 0],
                     [0, 1],
                     [1],
                     [1, 0],
                     [1, 0, 0],
                     [1, 0, 0, 0],
                     [0, 2],
                     ]
        symbol_table = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        str_num = str(num)
        answer = ""
        for i in range(len(str_num)):
            temp = ""
            for letter in num_table[int(str_num[i])]:
                temp = temp + symbol_table[letter + (len(str_num) - i - 1) * 2]
            answer = answer + temp
        return answer
