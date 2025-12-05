# Moo_operation
 
import sys
def solve():
    input = sys.stdin.readline
    Q = int(input())
    for _ in range(Q):
        s = input().strip()
        n = len(s)

        if n < 3:
            print(-1)
            continue

        best = -1  

        for i in range(n - 2):
            t = s[i:i+3]   
            if t == "MOO":
                cost = n - 3
            elif t == "MOM" or t == "OOO":
                cost = n - 2
            elif t == "OOM":
                cost = n - 1
            else:
                continue  

            if best == -1 or cost < best:
                best = cost

        print(best)

if __name__ == "__main__":
    solve()

# Watching_Mooloo

import sys
def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    days = list(map(int, input().split()))

    cur_start = days[0]
    cur_end = days[0]
    price = 0

    for i in range(1, N):
        d = days[i]
        gap = d - cur_end - 1 

        if gap < K:
            cur_end = d
        else:
            price += (cur_end - cur_start + 1) + K
            cur_start = d
            cur_end = d
    price += (cur_end - cur_start + 1) + K

    print(price)

solve()
        