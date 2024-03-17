# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         products.sort()
#         # common prefix
#         result = []
        
#         n = len(searchWord)
#         candidates = products.copy() # candidates recommendations
#         for i in range(n):
#             candi = []
#             for cand in candidates:
#                 if len(cand) > i and searchWord[i]==cand[i]:
#                     candi.append(cand)
#             if len(candi) > 3:
#                 result.append(candi[:3])
#             else:
#                 result.append(candi)
#             # print(candi)
#             candidates = candi.copy()

#         return result

class TrieNode:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.next:
                node.next[w] = TrieNode()
            node = node.next[w]
        node.isEnd = True 

    def hasPrefix(self, pre):
        node = self.root 
        for w in pre:
            if w not in node.next:
                return False 
            node = node.next[w]
        return True



class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        trie = Trie()
        trie.insert(searchWord)
        result = []
        n = len(searchWord)
        for i in range(n):
            result.append([])
            for p in products:
                if len(result[-1]) == 3:
                    break
                if len(p) >= i + 1 and trie.hasPrefix(p[:i+1]):
                    result[-1].append(p)
        return result
