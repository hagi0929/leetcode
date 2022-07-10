class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp_odd = [[]]
        dp_even = [[]]
        for i in range(len(s)):
            dp_odd[0].append(i)
        for i in range(len(s) - 1):
            dp_even[0].append(i)
        weight = 0
        for weight in range(len(s) + 1):
            if len(dp_odd[-1]) or len(dp_even[-1]):
                dp_odd.append([])
                dp_even.append([])
                for odd in dp_odd[weight]:
                    if odd - weight >= 0 and odd + weight < len(s):
                        if s[odd - weight] == s[odd + weight]:
                            dp_odd[weight + 1].append(odd)
                for even in dp_even[weight]:
                    if even - weight >= 0 and even + weight + 1 < len(s):
                        if s[even - weight] == s[even + 1 + weight]:
                            dp_even[weight + 1].append(even)
        if dp_even[-2]:
            return s[dp_even[-2][0] - (len(dp_even) - 3):dp_even[-2][0] + 2 + (len(dp_even) - 3)]
        else:
            return s[dp_odd[-2][0] - (len(dp_odd) - 3):dp_odd[-2][0] + 1 + (len(dp_odd) - 3)]
