class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        counter = 0
        repeat = ""
        weight = ceil(len(b)/len(a))
        repeat = a*weight
        if b in repeat:
            return weight
        elif b in repeat+a:
            return weight+1
        else:
            return -1


# class Solution:
#     def repeatedStringMatch(self, a: str, b: str) -> int:
#         weights = ceil(len(b)/len(a))
#         for t in weights, weights+1:
#             if b in a*t:
#                 return t
#         return -1
