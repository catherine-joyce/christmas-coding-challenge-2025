class Solution:
    def lengthOfLastWord(self, s: str) -> str:
        return len(s.strip().split(" ")[-1])
