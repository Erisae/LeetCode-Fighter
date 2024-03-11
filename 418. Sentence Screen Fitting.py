class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # greedy wont pass -> actually there is a pattern
        # calculate the number of words parsed assuming starting from each idx

        oneLine = defaultdict(lambda: (0, 0)) # idx -> (next idx, +1) 
        rowIdx = 0
        colIdx = 0
        wordIdx = 0
        res = 0
        while rowIdx < rows:
            # new row starting with sentence[wordIdx]
            if wordIdx in oneLine.keys():
                res += oneLine[wordIdx][1]
                wordIdx = oneLine[wordIdx][0]
                colIdx = 0
                rowIdx += 1
            else:
                count = 0
                wordIdxSt = wordIdx
                while colIdx + len(sentence[wordIdx]) - 1 < cols:
                    colIdx += len(sentence[wordIdx]) + 1 # next start col
                    wordIdx += 1
                    if wordIdx >= len(sentence):
                        count += 1
                        wordIdx = 0
                oneLine[wordIdxSt] = (wordIdx, count)
                res += count
                colIdx = 0
                rowIdx += 1
        return res

'''
1. the pattern is not simple, since loop might not be 0.232323, but 0.23445656, there is a possibility of sinking into the loop in the mid way
2. greedy would result in time limit
'''
                