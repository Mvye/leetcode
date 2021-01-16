class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverseX = int(str(x)[::-1])
        if x == reverseX:
            return True
        else:
            return False
