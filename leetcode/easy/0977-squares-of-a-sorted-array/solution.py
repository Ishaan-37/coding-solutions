class Solution:
    def sortedSquares(self, nums):

        negative = []
        positive = []

        # Separate negative and positive numbers
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)

        # If there are no negative numbers
        if len(negative) == 0:
            return [x * x for x in positive]

        # If there are no positive numbers
        if len(positive) == 0:
            result = [x * x for x in negative]
            result.reverse()
            return result

        # Square the negative numbers and reverse them
        negative = [x * x for x in negative][::-1]

        # Square the positive numbers
        positive = [x * x for x in positive]

        # Store the sizes of both arrays
        n = len(negative)
        m = len(positive)

        # Store the final sorted squares
        result = []

        # Initialize two pointers
        i = 0
        j = 0

        # Merge the two sorted arrays
        while i < n and j < m:
            if negative[i] <= positive[j]:
                result.append(negative[i])
                i += 1
            else:
                result.append(positive[j])
                j += 1

        # Add remaining elements from negative array
        while i < n:
            result.append(negative[i])
            i += 1

        # Add remaining elements from positive array
        while j < m:
            result.append(positive[j])
            j += 1

        # Return the sorted squares
        return result