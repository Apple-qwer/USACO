#Photoshoot2

def solve():
    import sys 
    input = sys.stdin.readline 
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    o = n - 1
    answer = 0 

    while x != y: 
        if x[o] != y[o]: 
            for j in range(len(y), 0, -1): 
                if j > 0: 
                    if x[o] == y[j]: 
                        x = x[j-1:] + x[o] + x[:j+1]
                        answer += 1
                        break 
                else: 
                    if x[o] == y[j]: 
                        x = x[o] + x[:j+1]
                        answer += 1
                        break 
                    
        else: 
            o -= 1 
    print(answer)

#Air Cownditioning

def solve():
    import sys
    input = sys.stdin.readline
    n = int(input())
    goal = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    diff = [] 
    for i in range(n): 
        diff.append(goal[i] - nums[i])
    ans = 0 
    while diff != [0] * n:  
        for i in range(n): 
            if diff[i] > 0: 
                diff[i] -= 1
                if i + 1 < n and diff[i + 1] <= 0: 
                    ans += 1 
            elif diff[i] < 0: 
                diff[i] += 1
                if i + 1 < n and diff[i + 1] >= 0: 
                    ans += 1
            if i == n: 
                ans += 1
    print(ans)

if __name__ == "__main__": 
    solve()

#Non-Transitive Dice

def solve():
    import sys 
    input = sys.stdin.readline 
    n = int(input())
    for i in range(n):
        nums = list(map(int, input().split()))
        A = nums[:4]
        B = nums[4:]
        score = 0
        for i in A:
            for j in B:
                if i > j:
                    score += 1
                elif i < j:
                    score -= 1
        if score < 0:
            A,B = B,A 
        possible = False 
        for c1 in range(1, 11): 
            for c2 in range(1,11): 
                for c3 in range(1,11): 
                    for c4 in range(1,11): 
                        C = [c1,c2,c3,c4]
                        score_bc = 0
                        for i in B:
                            for j in C:
                                if i > j:
                                    score_bc += 1
                                elif i < j:
                                    score_bc -= 1
                        if score_bc <= 0:
                            continue
                        score_ca = 0
                        for i in C:
                            for j in A:
                                if i > j:
                                    score_ca += 1
                                elif i < j:
                                    score_ca -= 1
                        if score_ca <= 0:
                            continue
                        possible = True 
                        break 
                    if possible: 
                        break 
                if possible: 
                    break 
            if possible: 
                break 
        if possible: 
            print("Yes")
        else: 
            print("No")
if __name__ == "__main__":
    solve()

#Counting Liars

def solve(): 
    import sys 
    input = sys.stdin.readline 
    n = int(input())
    cows = []
    for _ in range(n):
        t, p = input().split()
        p = int(p)
        cows.append((t, p))
    ans = [n] 
    for i in range(n): 
        true = cows[i][1]
        lies = 0 
        for j in range(n): 
            if j == i: 
                continue 
            if cows[j][0] == "G": 
                if cows[j][1] > true:
                    lies += 1 
            elif cows[j][1] < true: 
                lies += 1
        ans.append(lies)
    print(min(ans))
if __name__ == "__main__":
    solve()