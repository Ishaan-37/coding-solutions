class Solution(object):
    def characterReplacement(self, s, k):

        # Left pointer
        left = 0

        # Frequency dictionary
        freq = {}

        # Highest frequency inside current window
        max_freq = 0

        # Final answer
        ans = 0

        # Expand window
        for right in range(len(s)):

            # Current character
            ch = s[right]

            # Increase frequency
            freq[ch] = freq.get(ch, 0) + 1

            # Update maximum frequency
            if freq[ch] > max_freq:
                max_freq = freq[ch]

            # Current window size
            window = right - left + 1

            # If more than k replacements are needed
            while window - max_freq > k:

                # Remove left character
                freq[s[left]] -= 1

                # Move left pointer
                left += 1

                # Update window size
                window = right - left + 1

            # Update answer
            if window > ans:
                ans = window

        return ans