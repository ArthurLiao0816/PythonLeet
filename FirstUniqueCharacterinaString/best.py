import string


class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = 1e5
        for c in string.ascii_lowercase:
            l = s.find(c)
            r = s.rfind(c)
            if l == r != -1:
                a = min(a, l)
        return a if a < 1e5 else -1


print(string.ascii_lowercase)
