class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        DP = {}
        nums.sort()
        positive = []
        minVal = 10000000000000
        for i in range(0, len(nums) - 2):
            if DP.get(nums[i]):
                continue
            else:
                DP[nums[i]] = True
                left = i + 1
                right = len(nums) - 1
                while left != right:
                    sumLR = nums[left] + nums[right]
                    if sumLR == -target:
                        right -= 1
                    elif sumLR > -target:
                        right -= 1
                    elif sumLR < -target:
                        left += 1
                    val = abs(nums[left] + nums[right] + nums[i] - target)
                    if minVal > val:
                        minVal = val
                        answer = nums[left] + nums[right] + nums[i]

        return answer