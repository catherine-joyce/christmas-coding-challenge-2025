class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_string = str(x)
        i = 0
        j = len(int_string) - 1
        while i < j:
            if int_string[i] == int_string[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
