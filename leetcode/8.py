class Solution:
    def myAtoi(self, s: str) -> int:
        numlists = []
        hadPM = False
        hadnum = False
        for i in range(len(s)):
            if s[i].isnumeric():
                hadnum = True
                numlists.append(i)
                hadPM = True
            elif s[i] == "+" or s[i] == "-":
                if hadPM or hadnum:
                    break
                else:
                    hadPM = True
            elif s[i] == " ":
                if hadPM or hadnum:
                    break
                continue
            else:
                break
        print(numlists)
        if not numlists:
            return 0
        extracted = s[min(numlists):max(numlists) + 1]
        num = int(extracted)

        if min(numlists) - 1 >= 0 and s[min(numlists) - 1] == "-":
            num = -num

        if 2 ** 31 - 1 < num:
            return 2 ** 31 - 1

        elif num < -2 ** 31:
            return -2 ** 31
        return num