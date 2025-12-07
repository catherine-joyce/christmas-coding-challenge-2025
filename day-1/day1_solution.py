class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int("".join([str(element) for element in digits]))
        num += 1
        return [int(element) for element in list(str(num))]
