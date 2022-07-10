class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        ans = []
        for N in range(numRows):
            if N >= len(s):
                break
            temp = [s[N]]
            init = N
            left = True
            while True:
                if left:
                    adder = (numRows - 1 - N) * 2
                    left = False
                else:
                    adder = N * 2
                    left = True
                if adder:
                    init += adder
                    if init >= len(s):
                        break
                    else:
                        temp.append(s[init])
            ans.append("".join(temp))
        print(ans)
        return "".join(ans)
