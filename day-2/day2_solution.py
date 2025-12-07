class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        friends_set = set(friends)
        return [x for x in order if x in friends_set]
