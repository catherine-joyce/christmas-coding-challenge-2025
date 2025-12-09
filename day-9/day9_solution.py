class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        new_string = ""
        for x in s:
            x = list(x)
            i = 0 
            j = len(x) -1 
            while i < j:
                x[i], x[j] = x[j], x[i]
                i += 1
                j -= 1
            x_string = "".join(x)
            new_string = new_string + x_string + " "
        return new_string.strip()