class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        max_len = 0
        left = 0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0) + 1
            max_freq = max(count[s[right]], max_freq)

            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, (right - left + 1))
        return max_len

