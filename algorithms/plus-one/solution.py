class Solution(object):
    def plusOne(self, digits):
        s = ""

        for i in digits:
            s += str(i)

        num = int(s)
        nums = num +1
        arr = list(map(int, str(nums)))
        return arr




        
      