class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Dictionary to store the count of each character 'a', 'b', 'c' in the current window
        count = {'a': 0, 'b': 0, 'c': 0}
        
        # Left pointer for the sliding window
        left = 0 
        
        # Result variable to store the total count of valid substrings
        result = 0

        # Iterate over the string using the right pointer
        for right in range(len(s)):
            # Increase the count of the current character in the window
            count[s[right]] += 1

            # Check if the window contains at least one occurrence of all three characters
            while all(count.values()):  
                # If valid, all substrings starting from `left` to `right` and extending till end are valid
                # `len(s) - right` gives the number of substrings that can be formed
                result += len(s) - right  

                # Now shrink the window from the left side
                count[s[left]] -= 1  # Reduce the count of the character at `left`
                left += 1  # Move left pointer forward

        # Return the total count of valid substrings
        return result
