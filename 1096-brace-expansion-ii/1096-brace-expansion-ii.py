class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def solve(s, i):
            result = set()
            current = {""}

            while i < len(s) and s[i] != '}':
                
                if s[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1

                elif s[i].islower():
                    new = set()

                    for a in current:
                        new.add(a + s[i])

                    current = new
                    i += 1

                else:
                    temp, i = solve(s, i + 1)

                    new = set()

                    for a in current:
                        for b in temp:
                            new.add(a + b)

                    current = new

            result.update(current)

            return result, i + 1

        answer, _ = solve(expression, 0)

        return sorted(answer)