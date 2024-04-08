class TrieNode:
    def __init__(self):
        self.isEnd = -1 # should be the index in array
        self.next = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, index):
        node = self.root
        for c in word:
            if not c in node.next:
                node.next[c] = TrieNode()
            node = node.next[c]
        node.isEnd = index

    def search(self, word):
        node = self.root
        for c in word:
            node = node.next.get(c, None)
            if not node:
                return [-1]
        # then match for every word after node using bfs
        result = []
        queue = deque()
        queue.append(node)

        while queue:
            node = queue.popleft()
            if node.isEnd >= 0:
                result.append(node.isEnd)
            for nextNode in node.next.values():
                queue.append(nextNode)
        return result


class WordFilter:
    # two tries -> prefix and suffix, search both way and return intersection of index

    def __init__(self, words: List[str]):
        self.prefixTrie = Trie()
        self.suffixTrie = Trie()

        for idx, word in enumerate(words):
            self.prefixTrie.insert(word, idx)
            self.suffixTrie.insert(word[::-1], idx)


    def f(self, pref: str, suff: str) -> int:
        res_prefix = self.prefixTrie.search(pref)
        res_suffix = self.suffixTrie.search(suff[::-1])

        if res_prefix == [-1] or res_suffix == [-1]:
            return -1
        res = list(set(res_prefix).intersection(set(res_suffix)))
        if not res:
            return -1

        return max(res)



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)