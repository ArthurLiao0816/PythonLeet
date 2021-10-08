class Solution:
    def firstUniqChar(self, s: str) -> int:
        for c in s:
            if s.count(c) == 1:
                return s.index(c)
        return -1


table = {'a': 1, 'b': 2}
print(table[0])


class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = {}
        for c in s:
            if c not in table:
                table[c] = s.index(c)

            else:
                table[c] = -1
        print(table)
        for idx, value in table.items():
            print(value)
            if value != -1:
                return value
        return -1
