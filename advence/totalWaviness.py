class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        def count_upto(n):
            if n <= 0:
                return 0

            s = str(n)
            L = len(s)
            memo = {}

            def dp(pos, tight, started, prev2, prev1):
                if pos == L:
                    return (1, 0)

                key = (pos, tight, started, prev2, prev1)

                if key in memo:
                    return memo[key]

                if tight:
                    limit = int(s[pos])
                else:
                    limit = 9

                total_count = 0
                total_wave = 0

                for d in range(limit + 1):
                    new_tight = tight and (d == limit)

                    # Not started ye and if selected 0
                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, new_tight, False, -1, -1)
                        total_count += cnt
                        total_wave += wav

                    else:
                        # First start
                        if not started:
                            cnt, wav = dp(pos + 1, new_tight, True, -1, d)
                            total_count += cnt
                            total_wave += wav

                        else:
                            add = 0

                            # If have prev2, prev1, d exist 
                            if prev2 != -1:
                                if prev1 > prev2 and prev1 > d:
                                    add = 1
                                elif prev1 < prev2 and prev1 < d:
                                    add = 1

                            cnt, wav = dp(pos + 1, new_tight, True, prev1, d)

                            total_count += cnt
                            total_wave += wav + add * cnt

                memo[key] = (total_count, total_wave)
                return memo[key]

            return dp(0, True, False, -1, -1)[1]

        return count_upto(num2) - count_upto(num1 - 1)