class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        def recursive(num):
            if num > n:
                return
            result.append(num)
            if num * 10 <= n:
                recursive(num * 10)
            if num + 1 <= n and (num % 10 < 9):
                recursive(num + 1)
        
        recursive(1)
        return result