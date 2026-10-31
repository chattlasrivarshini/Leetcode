class Solution(object):
    def moveZeroes(self, nums):
        write = 0
    
    # Read pointer scans the list
        for read in range(len(nums)):
        # If we find a non-zero element, swap it to the front
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            
        return nums
        

      
    
    