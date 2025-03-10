class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        word = []
        left = 0
        n = len(s)

        while(left < n):
            if s[left] == " ":
                left += 1
                continue

            right = left
            while right < n and s[right] != " ":
                right += 1

            word.append(s[left:right])
            left = right

        return " ".join(reversed(word))
        