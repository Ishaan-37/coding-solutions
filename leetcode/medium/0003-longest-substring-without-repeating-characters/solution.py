class Solution(object):
    def lengthOfLongestSubstring(self, s):

        # Dictionary to store the frequency of characters
        char_count = {}

        # Left pointer of the sliding window
        left = 0

        # Stores the maximum length of a valid substring
        max_len = 0

        # Right pointer expands the window
        for right in range(len(s)):

            # Add the current character to the dictionary
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # If the current character is repeated,
            # shrink the window from the left
            while char_count[s[right]] > 1:

                # Remove the leftmost character
                char_count[s[left]] -= 1

                # Move the left pointer
                left += 1

            # Current window length
            current_len = right - left + 1

            # Update the maximum length
            if current_len > max_len:
                max_len = current_len

        # Return the answer
        return max_len