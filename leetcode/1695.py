class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        DP = [0]
        cutter = None
        last_came = [0]*(10**5)
        maxVal = 0
        for i, number in enumerate(nums):
            if cutter == None:
                DP.append(number)
                last_came[number] = i + 1
                cutter = 0
                maxVal = number
            else:
                if last_came[number] > cutter :
                    cutter = last_came[number]
                last_came[number] = i + 1
                DP.append(DP[i]+number)
                maxVal = max(DP[i+1] - DP[cutter], maxVal)
        return maxVal