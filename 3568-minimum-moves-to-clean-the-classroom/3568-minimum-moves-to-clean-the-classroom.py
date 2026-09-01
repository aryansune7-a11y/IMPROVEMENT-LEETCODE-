from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m, n = len(classroom), len(classroom[0])
        grid = classroom

        litter_bit = {}
        start = None
        for r in range(m):
            for c in range(n):
                ch = grid[r][c]
                if ch == 'S':
                    start = (r, c)
                elif ch == 'L':
                    litter_bit[(r, c)] = len(litter_bit)

        L = len(litter_bit)
        full_mask = (1 << L) - 1
        if full_mask == 0:
            return 0

        E1 = energy + 1
        M1 = full_mask + 1 
        NCELLS = m * n

        def encode(r, c, e, mask):
            return ((r * n + c) * E1 + e) * M1 + mask

        visited = bytearray(NCELLS * E1 * M1)

        sr, sc = start
        start_state = encode(sr, sc, energy, 0)
        visited[start_state] = 1
        q = deque([(sr, sc, energy, 0)])
        moves = 0

        litter_bit_grid = [[-1] * n for _ in range(m)]
        for (r, c), b in litter_bit.items():
            litter_bit_grid[r][c] = b

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()
                if mask == full_mask:
                    return moves
                if e == 0:
                    continue

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    cell = grid[nr][nc]
                    if cell == 'X':
                        continue

                    new_e = energy if cell == 'R' else e - 1
                    bit = litter_bit_grid[nr][nc]
                    new_mask = mask | (1 << bit) if bit != -1 else mask

                    key = encode(nr, nc, new_e, new_mask)
                    if not visited[key]:
                        visited[key] = 1
                        q.append((nr, nc, new_e, new_mask))
            moves += 1

        return -1