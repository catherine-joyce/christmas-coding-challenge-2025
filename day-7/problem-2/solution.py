class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_string = ""
        for letter in s:
            if letter.isalpha() and ord(letter) <= 90:
                new_letter_ord = ord(letter) + 32
                new_string += chr(new_letter_ord)
            else:
                new_string += letter
        return new_string
        
        