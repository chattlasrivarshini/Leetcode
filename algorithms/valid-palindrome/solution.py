class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        s=''.join(c for c in s if c.isalnum())
        if s==s[::-1]:
            return True
        else:
            return False    