class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        # if k is even -> start from 10^(k/2-1), (10^(k/2-1) + x - 1)*10^(k/2) + reverse(10^(k/2-1) + x - 1)
        # if k is odd  -> start from 10^(k/2), (10^(k/2) + x - 1)*10^(k/2) + reverse %%%
        
        result = []

        if intLength % 2 == 0: # even
            for query in queries:
                front = (query - 1) + 10 ** (intLength / 2 - 1)
                if front >= 10 ** (intLength / 2):
                    result.append(-1)
                    continue
                back = 0
                num = front
                while num:
                    back = back * 10 + num % 10
                    num = int(num / 10)
                result.append(int(front * (10 ** (intLength / 2)) + back))
        else:
            for query in queries:
                front = (query - 1) + (10 ** int(intLength / 2))
                if front >= 10 ** (int(intLength / 2) + 1):
                    result.append(-1)
                    continue
                back = 0
                num = int(front / 10)
                while num:
                    back = back * 10 + num % 10
                    num = int(num / 10)
                result.append(front * (10 ** (int(intLength / 2))) + back)
        
        return result

                
