class Solution:
    def minSubArrayLen(self, target, nums):

        # Find the length of the array
        n = len(nums)

        # Left pointer of the sliding window
        left = 0

        # Stores the current window sum
        window_sum = 0

        # Initialize minimum length as infinity
        min_len = float('inf')

        # Expand the window by moving the right pointer
        for right in range(n):

            # Add the current element to the window sum
            window_sum += nums[right]

            # Shrink the window while the sum is
            # greater than or equal to the target
            while window_sum >= target:

                # Update the minimum length found so far
                min_len = min(min_len, right - left + 1)

                # Remove the leftmost element from the window
                window_sum -= nums[left]

                # Move the left pointer forward
                left += 1

        # If no valid subarray is found, return 0
        if min_len == float('inf'):
            return 0

        # Otherwise, return the minimum length
        return min_len