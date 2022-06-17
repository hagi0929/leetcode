class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashNum = {}
        sortedNums = sorted(nums)
        for i in sortedNums:
            hashNum[i] = hashNum.get(i, 0) + 1
        answer = set()
        fuckduplicate = {}
        def recursiveRight(dic, left, right):
            if right >= len(nums):
                return
            dic[sortedNums[right]] -= 1
            if dic.get(-(sortedNums[left] + sortedNums[right]), 0):
                answer.add(tuple([sortedNums[left], sortedNums[right], -(sortedNums[left] + sortedNums[right])]))
            recursiveRight(dic, left, right + 1)
            dic[sortedNums[right]] += 1

        for left in range(0, len(nums)):
            hashNum[sortedNums[left]] -= 1
            if fuckduplicate.get(sortedNums[left]):
                continue
            else:
                fuckduplicate[sortedNums[left]]=True
            recursiveRight(hashNum, left, left + 1)
        return answer

