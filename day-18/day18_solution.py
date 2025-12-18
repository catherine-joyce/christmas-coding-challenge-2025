class Solution:
    def isPrefix(self, word: str, s: str) -> bool:
        if len(word) > len(s):
            return False
        i = 0
        while i < len(word):
            if word[i] == s[i]:
                i += 1
            else:
                return False
        return True

    def countPrefixes(self, words: list[str], s: str) -> int:
        count = 0
        for word in words:
            if self.isPrefix(word, s):
                count += 1
        return count
