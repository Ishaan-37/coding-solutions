class Solution:
    def sortColors(self, nums):

        # Pointer for placing 0s
        low = 0

        # Current element being checked
        mid = 0

        # Pointer for placing 2s
        high = len(nums) - 1

        # Traverse until all elements are processed
        while mid <= high:

            # If current element is 0
            if nums[mid] == 0:

                # Swap with low pointer
                nums[low], nums[mid] = nums[mid], nums[low]

                # Move both pointers forward
                low += 1
                mid += 1

            # If current element is 1
            elif nums[mid] == 1:

                # Already in correct position
                mid += 1

            # If current element is 2
            else:

                # Swap with high pointer
                nums[mid], nums[high] = nums[high], nums[mid]

                # Move high pointer backward
                high -= 1

                # Do NOT increment mid
                # The swapped element needs to be checked