# Photoshoot2
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
            for j in range(len(y)): 
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

# Air cownditioning
def solve():
    import sys
    input = sys.stdin.readline
    n = int(input())
    desired = list(map(int, input().split()))
    current = list(map(int, input().split()))

    ans = 0
    

    while desired != current:
        i = 0
        if desired[i] != current[i]:
            x = desired[i] - current[i]
            j = i
            while j < n and (desired[j] - current[j]) * x > 0:
                current[j] += x // abs(x)  
                j += 1
            ans += 1
        else:
            i += 1
    print(ans)