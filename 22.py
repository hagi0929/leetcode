class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sets = {""}
        for i in range(n):
            temp = set()
            for elem in sets:
                temp.add(f"(){elem}")
                temp.add(f"({elem})")
                temp.add(f"{elem}()")
            sets = temp
        return sorted(list(sets), reverse=False)
