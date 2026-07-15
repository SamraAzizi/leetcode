class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        MOD = 10 ** 9 +7

        cur = [[0] * 201 for _ in range(201)]
        cur[0][0] = 1

        for x in nums:
            nxt = [[0] * 201 for _ in range(201)]

            for g1 in range(201):
                for g2 in range(201):
                    if cur[g1][g2] == 0:
                        continue
                    
                    ways = cur[g1][g2]
                    
                    nxt[g1][g2] = (nxt[g1][g2] + ways) % MOD

                    ng1 = x if g1 == 0 else gcd(g1,x)
                    nxt[ng1][g2]= (nxt[ng1][g2] + ways) % MOD

                    ng2 = x if g2 == 0 else gcd(g2,x)
                    nxt[g1][ng2]= (nxt[g1][ng2] + ways) % MOD
        
            cur = nxt

        ans = 0
        for g in range(1, 201):
            ans = (ans + cur[g][g]) % MOD
        return ans


        