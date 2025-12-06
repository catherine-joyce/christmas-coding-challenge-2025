class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        j = 0
        while j < len(haystack):
            if needle[i] == haystack[j]:
                i += 1
                j += 1
            elif needle[i] != haystack[j]:
                j -= (i - 1)
                i = 0
            if i == len(needle):
                return j - len(needle)
        return -1