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
1| 1
  ()
2| 1 1, 0.5 1 0.5
  ()() (())
3| 1 1 1, 0.5 1 1 0.5, 1 2, 2 1, 3
  ()()() (()()) ()(()) (())() ((()))
4| 1 1 1 1, 1 1 2,    1 2 1,   2 1 1,    1 3,    2 2,     3 1,      4
  ()()()() ()()(()) ()(())() (())()() ()((())) (())(()) ((()))() (((())))