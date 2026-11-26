class Solution:
    def canAliceWin(self, n: int) -> bool:
        remover = 10
        alice = True

        while n >= remover:
            n -= remover
            remover -= 1
            alice = not alice

        return not alice