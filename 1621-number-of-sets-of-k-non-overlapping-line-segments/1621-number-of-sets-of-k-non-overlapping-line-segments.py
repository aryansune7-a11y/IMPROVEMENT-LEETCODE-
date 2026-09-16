class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10**9 + 7

        def combination(n,k):
            ans = 1
            for i in range(1,k+1):
                ans = ans*(n-i+1)//i
            return ans    

        return combination(n + k - 1, 2 * k) % mod