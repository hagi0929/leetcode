class Solution:
    def reverse(self, x: int) -> int:
        if x >=0:
            num = int(str(x)[::-1])
            if 2**31 - 1> num > -2**31:
                return num
            else:
                return 0
        else:
            num = str(x)[::-1]
            if 2**31 - 1> int(num[:-1]) > -(2**31):
                return -int(num[:-1])
            else:
                return 0