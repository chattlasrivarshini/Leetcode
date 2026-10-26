class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        summ = 0 
        for i in range (n+1):
            summ = summ +i

        sum_of_nums = sum(nums)    

        return summ - sum_of_nums

        