# Leaders
def solve():
    import sys
    input = sys.stdin.readline
    n = int(input())
    breeds = input().strip()
    x = list(map(int, input().split()))

    min_g = n
    max_g = -1
    min_h = n
    max_h = -1

    for i in range(n):
        if breeds[i] == 'G':
            min_g = min(min_g, i)
            max_g = max(max_g, i)
        else:
            min_h = min(min_h, i)
            max_h = max(max_h, i)

    g_candidates = [i for i in range(n) if breeds[i] == 'G']
    h_candidates = [i for i in range(n) if breeds[i] == 'H']

    count = 0

    for g in g_candidates:
        for h in h_candidates:
            g_list_valid = False
            h_list_valid = False

            g_end = x[g] - 1
            h_end = x[h] - 1

            if g <= min_g and g_end >= max_g:
                g_list_valid = True
            elif g <= h <= g_end:
                g_list_valid = True


            if h <= min_h and h_end >= max_h:
                h_list_valid = True
  
            elif h <= g <= h_end:
                h_list_valid = True

            if g_list_valid and h_list_valid:
                count += 1

    print(count)
if __name__ == "__main__":
    solve()

# feb 
from itertools import product

def solve():
    import sys
    input = sys.stdin.readline

    n = int(input())
    s = input().strip()

    positions = [i for i in range(n) if s[i] == 'F']
    k = len(positions)

    results = set()

    for combo in product('BE', repeat=k):
        temp = list(s)
        for j in range(k):       
            idx = positions[j]
            ch = combo[j]
            temp[idx] = ch
        excitement = 0
        for i in range(1, n):
            if temp[i] == temp[i-1]:
                excitement += 1
        results.add(excitement)

    results = sorted(results)
    print(len(results))
    for r in results:
        print(r)

if __name__ == "__main__":
    solve()
# alchemy
def solve():
    import sys
    input = sys.stdin.readline

    N = int(input())  
    metals = list(map(int, input().split()))  
    K = int(input()) 

    recipe = [None] * N  

    for _ in range(K):
        parts = list(map(int, input().split()))
        L = parts[0]   
        M = parts[1]      
        ingredients = parts[2:2 + M]  
        recipe[L - 1] = [x - 1 for x in ingredients] 

    changed = True
    while changed:
        changed = False
        for i in range(N):
            if recipe[i] is None:
                continue
            ingredients = recipe[i]


if __name__ == "__main__": 
    solve()