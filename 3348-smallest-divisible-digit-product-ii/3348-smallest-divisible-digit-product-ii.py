import math

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        counts = {2: 0, 3: 0, 5: 0, 7: 0}
        temp_t = t
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                counts[p] += 1
                temp_t //= p

        if temp_t > 1:
            return "-1"

        def min_digits_needed(c2, c3, c5, c7):

            d9 = c3 // 2
            r3 = c3 % 2
            
            d8 = c2 // 3
            r2 = c2 % 3
            
            d7 = c7
            d5 = c5
            
            d6 = 0
            if r3 == 1 and r2 == 1:
                d6 = 1
                r3, r2 = 0, 0
            elif r3 == 1 and r2 == 2:
                d6 = 1
                r3 = 0
                r2 = 1
                
            d4 = r2 // 2
            r2 %= 2
            
            d3 = r3
            d2 = r2
            
            return d9 + d8 + d7 + d6 + d5 + d4 + d3 + d2

        def get_smallest_suffix(rem_len, c2, c3, c5, c7):

            res = []
            for _ in range(rem_len):
                for d in range(1, 10):

                    fc2 = 0
                    td = d
                    while td % 2 == 0: fc2 += 1; td //= 2
                    fc3 = 0
                    while td % 3 == 0: fc3 += 1; td //= 3
                    fc5 = 1 if d == 5 else 0
                    fc7 = 1 if d == 7 else 0
                    
                    nc2 = max(0, c2 - fc2)
                    nc3 = max(0, c3 - fc3)
                    nc5 = max(0, c5 - fc5)
                    nc7 = max(0, c7 - fc7)
                    
                    if min_digits_needed(nc2, nc3, nc5, nc7) <= rem_len - 1 - len(res):
                        res.append(str(d))
                        c2, c3, c5, c7 = nc2, nc3, nc5, nc7
                        break
            return "".join(res)

        n = len(num)
        
        first_zero = num.find('0')
        if first_zero != -1:

            num = num[:first_zero] + '0' + '0' * (n - 1 - first_zero)

        pref_c2 = [0] * (n + 1)
        pref_c3 = [0] * (n + 1)
        pref_c5 = [0] * (n + 1)
        pref_c7 = [0] * (n + 1)
        
        for i in range(n):
            d = int(num[i])
            pref_c2[i+1] = pref_c2[i]
            pref_c3[i+1] = pref_c3[i]
            pref_c5[i+1] = pref_c5[i]
            pref_c7[i+1] = pref_c7[i]
            if d > 0:
                td = d
                while td % 2 == 0: pref_c2[i+1] += 1; td //= 2
                while td % 3 == 0: pref_c3[i+1] += 1; td //= 3
                if d == 5: pref_c5[i+1] += 1
                if d == 7: pref_c7[i+1] += 1

        if '0' not in num:
            req2 = max(0, counts[2] - pref_c2[n])
            req3 = max(0, counts[3] - pref_c3[n])
            req5 = max(0, counts[5] - pref_c5[n])
            req7 = max(0, counts[7] - pref_c7[n])
            if req2 == 0 and req3 == 0 and req5 == 0 and req7 == 0:
                return num

        for i in range(n - 1, -1, -1):
            if first_zero != -1 and i > first_zero:
                continue
                
            start_digit = int(num[i]) + 1
            for d in range(start_digit, 10):
                fc2 = 0; td = d
                while td % 2 == 0: fc2 += 1; td //= 2
                fc3 = 0
                while td % 3 == 0: fc3 += 1; td //= 3
                fc5 = 1 if d == 5 else 0
                fc7 = 1 if d == 7 else 0
                
                cur2 = pref_c2[i] + fc2
                cur3 = pref_c3[i] + fc3
                cur5 = pref_c5[i] + fc5
                cur7 = pref_c7[i] + fc7
                
                rem2 = max(0, counts[2] - cur2)
                rem3 = max(0, counts[3] - cur3)
                rem5 = max(0, counts[5] - cur5)
                rem7 = max(0, counts[7] - cur7)
                
                rem_len = n - 1 - i
                if min_digits_needed(rem2, rem3, rem5, rem7) <= rem_len:
                    prefix = num[:i] + str(d)
                    suffix = get_smallest_suffix(rem_len, rem2, rem3, rem5, rem7)
                    return prefix + suffix

        target_len = max(n + 1, min_digits_needed(counts[2], counts[3], counts[5], counts[7]))
        return get_smallest_suffix(target_len, counts[2], counts[3], counts[5], counts[7])