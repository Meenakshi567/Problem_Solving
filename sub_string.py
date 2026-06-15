class Solution:
    def longestUniqueSubstr(self, s: str) -> int:
        # Array to store the last seen position of characters (initialized to -1)
        last_seen = [-1] * 26
        max_len = 0
        left = 0
        
        for right in range(len(s)):
            char_idx = ord(s[right]) - ord('a')
            
            # If the character was seen inside the current window, move the left pointer
            if last_seen[char_idx] >= left:
                left = last_seen[char_idx] + 1
                
            # Update the last seen index of the character
            last_seen[char_idx] = right
            
            # Calculate and update the maximum length
            max_len = max(max_len, right - left + 1)
            
        return max_len
