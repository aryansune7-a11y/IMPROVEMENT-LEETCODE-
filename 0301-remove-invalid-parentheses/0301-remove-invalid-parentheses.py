class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def valid(s):
            count = 0

            for ch in s:
                if ch == "(":
                    count += 1
                elif ch == ")":
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = [s]
        visited = {s}

        while queue:

            ans = []

            for curr in queue:
                if valid(curr):
                    ans.append(curr)

            if ans:
                return list(set(ans))

            new_queue = []

            for curr in queue:
                for i in range(len(curr)):

                    if curr[i] not in "()":
                        continue

                    new = curr[:i] + curr[i + 1:]

                    if new not in visited:
                        visited.add(new)
                        new_queue.append(new)

            queue = new_queue

        return [""]