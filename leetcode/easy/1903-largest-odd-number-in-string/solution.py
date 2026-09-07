class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num)-1, -1, -1): #Last index se start karke, har baar 1 step peeche jaate hue first index tak loop karta hai.
            if int(num[i]) % 2:
                return num[:i+1] #String ke start (index 0) se index i tak ke characters leta hai; +1 isliye kyunki slicing mein ending index include nahi hota
        return ""