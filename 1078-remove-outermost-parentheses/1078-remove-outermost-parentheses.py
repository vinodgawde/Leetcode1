class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        counter = 0
        for ch in s:
            if ch == '(':
                if counter > 0:
                    ans += ch
                counter += 1
            else:
                counter -= 1
                if counter > 0:
                    ans += ch
        return ans