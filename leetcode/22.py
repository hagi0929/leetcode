class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sets = []

        def back(current, left, right):
            if left + right == n * 2:
                sets.append(current)
            if left < n:
                back(current + "(", left + 1, right)
            if right < left:
                back(current + ")", left, right + 1)

        back("", 0, 0)
        return sets