class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        table = {}
        counter = 0
        for domino in dominoes:
            cur = tuple(sorted(domino))

            if cur not in table:
                table[cur] = 0
            else:
                table[cur] += 1
                counter += table[cur]
        return counter
