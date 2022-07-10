class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        maxArea = 0
        while True:
            if right == left:
                break
            else:
                maxArea = max(min(height[left], height[right]) * (right - left), maxArea)

                if height[left] >= height[right]:
                    right -= 1
                else:
                    left += 1

        return maxArea
