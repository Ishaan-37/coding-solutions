class Solution:
    def sortColors(self, nums):

        # Count the number of 0s, 1s, and 2s
        count0 = 0
        count1 = 0
        count2 = 0

        # Traverse the array once to count each value
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        # Start filling the array from index 0
        index = 0

        # Fill all the 0s
        while count0 > 0:
            nums[index] = 0
            index += 1
            count0 -= 1

        # Fill all the 1s
        while count1 > 0:
            nums[index] = 1
            index += 1
            count1 -= 1

        # Fill all the 2s
        while count2 > 0:
            nums[index] = 2
            index += 1
            count2 -= 1