def solve():
    import sys
    from itertools import combinations
    input = sys.stdin.readline

    N, M = map(int, input().split())
    spotty = [input().strip() for _ in range(N)]
    plain  = [input().strip() for _ in range(N)]

    ans = 0
    for a, b, c in combinations(range(M), 3):
        seen = []

        for s in spotty:
            seen.append((s[a], s[b], s[c]))

        ok = True
        for p in plain:
            if (p[a], p[b], p[c]) in seen:
                ok = False
                break

        if ok:
            ans += 1

    print(ans)

if __name__ == "__main__":
    solve()
