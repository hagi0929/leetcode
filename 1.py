class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_num = sorted(nums)
        dick = {}
        for i, elem in enumerate(nums):
            if elem in dick.keys():
                dick[elem].append(i)
            else:
                dick[elem] = [i]
        left = 0
        right = len(nums) - 1
        while True:
            sums = sorted_num[left] + sorted_num[right]
            if sums == target:
                break
            elif sums > target:
                right -= 1
            else:
                left += 1
        l1 = dick[sorted_num[left]].pop()
        l2 = dick[sorted_num[right]].pop()
        return [l1, l2]