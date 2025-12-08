class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s) 
        for x in range(0, len(s), k+k):
            i = x 
            j = i + (k -1)
            if (x + k) > len(s):
               j = len(s)-1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)