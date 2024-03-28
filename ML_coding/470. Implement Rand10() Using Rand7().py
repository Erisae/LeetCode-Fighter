# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # each number returned as an equal probability
        # 8a + b, minimal is 9, maximum is 64.
        while True:
            a = rand7()
            b = rand7()
            num = a + (b - 1)* 7
            if num <= 40:
                return (num - 1) % 10 + 1
                                                                                                                                                                                                                             
        