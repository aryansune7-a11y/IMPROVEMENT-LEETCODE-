class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        seq = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []

        def backtrack(index, current):

            if index == len(digits):
                ans.append(current)
                return

            for ch in mapping[digits[index]]:

                current += ch

                backtrack(index + 1, current)

                current = current[:-1]

        backtrack(0, "")

        return ans