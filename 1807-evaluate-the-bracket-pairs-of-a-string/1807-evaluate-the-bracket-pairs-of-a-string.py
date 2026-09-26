class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        new = ""

        d = {}
        for key, value in knowledge:
            d[key] = value

        i = 0

        while i < len(s):

            if s[i] == "(":

                j = i + 1

                while s[j] != ")":
                    j += 1

                key = s[i + 1:j]
                if key in d:
                    new += d[key]
                else:
                    new += "?"

                i = j + 1

            else:
                new += s[i]
                i += 1

        return new