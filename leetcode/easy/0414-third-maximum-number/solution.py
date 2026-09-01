class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums)) #set(nums) duplicates hata deta hai: Lekin set ek set deta hai, list nahi.Isliye:list(set(nums)banega
        nums.sort(reverse=True) #reverse=True ka matlab:largest se smallest

        if len(nums) >= 3: #Ab check kar rahe hain:Kya kam se kam 3 distinct numbers hain?:len(nums) = list mein kitne elements hain.
            return nums[2] #Agar 3 ya usse zyada distinct numbers hain, toh third maximum return karo.
        else:
            return nums[0] #Third maximum exist na kare, toh maximum return karo.
        
        