class Solution:
    def lengthOfLastWord(self, s: str) -> str:
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])
