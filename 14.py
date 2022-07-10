class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        i = 0
        while True:
            try:
                if len(set([st[i] for st in strs])) == 1:
                    i += 1
                else:
                    answer = strs[0][:i]
                    break
            except:
                answer = strs[0][:i]
                break

        return answer
