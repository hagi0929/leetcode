class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp = [0]
        appeared = {
        }
        for i, letter in enumerate(s):
            if letter not in appeared.keys():
                appeared[letter] = 0
            dp.append(min(dp[i] + 1, i+1-appeared[letter]))
            appeared[letter] = i+1
        return max(dp)