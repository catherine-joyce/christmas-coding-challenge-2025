class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join([str(element) for element in digits]))
        num += 1
        return [int(element) for element in list(str(num))]
