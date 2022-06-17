class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        DP = {}
        answer = set()
        nums.sort()
        for i in range(0, len(nums) - 2):
            if DP.get(nums[i]):
                continue
            else:
                DP[nums[i]] = True
                left = i + 1
                right = len(nums) - 1
                while left != right:
                    sumLR = nums[left] + nums[right]
                    if sumLR == -nums[i]:
                        answer.add(tuple([nums[left], nums[right], nums[i]]))

                        right -= 1
                    elif sumLR > -nums[i]:
                        right -= 1

                    elif sumLR < -nums[i]:
                        left += 1
        return answer
