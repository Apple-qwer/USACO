# Hungry Cow 
def solve():
    import sys
    input = sys.stdin.readline

    N, T = map(int, input().split())
    deliveries = []
    for _ in range(N):
        d, b = map(int, input().split())
        deliveries.append((d, b))
   

    barn = 0        
    eaten = 0      
    cur_day = 1      
    for d, b in deliveries:
        if cur_day <= T:
            gap_end = min(T, d - 1)
            if gap_end >= cur_day:
                gap_days = gap_end - cur_day + 1
                eat_here = min(barn, gap_days)
                eaten += eat_here
                barn -= eat_here

        barn += b


        if cur_day < d:
            cur_day = d

    if cur_day <= T:
        gap_days = T - cur_day + 1
        eat_here = min(barn, gap_days)
        eaten += eat_here

    print(eaten)


if __name__ == "__main__":
    solve()

# Cow_college

def solve():
    import sys
    input = sys.stdin.readline

    n = int(input())
    tuition = list(map(int, input().split()))


    freq = {}
    for t in tuition:
        freq[t] = freq.get(t, 0) + 1

    unique = sorted(freq.keys())

    best_money = 0
    best_tuition = 0

    
    Can_pay = 0


    for t in reversed(unique):
        Can_pay += freq[t]    
        money = Can_pay * t

        if money > best_money:
            best_money = money
            best_tuition = t
        elif money == best_money and t < best_tuition:
            best_tuition = t

    print(best_money, best_tuition)

if __name__ == "__main__":
    solve()