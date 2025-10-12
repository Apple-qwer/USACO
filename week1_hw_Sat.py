# Sleeping_in_class 
def solve():
    import sys
    input = sys.stdin.readline
    
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        c = 0  

        if N == 1:
            print(0)
            continue

        while len(arr) > 2:
            max_val = max(arr)
            merged = False
            for i in range(len(arr)):
                if i < len(arr) - 1 and arr[i] < max_val and arr[i+1] < max_val:
                    new_val = arr[i] + arr[i+1]
                    arr = arr[:i] + [new_val] + arr[i+2:]
                    c += 1
                    merged = True
                    break
                elif i > 0 and arr[i] < max_val and arr[i-1] < max_val:
                    new_val = arr[i] + arr[i-1]
                    arr = arr[:i-1] + [new_val] + arr[i+1:]
                    c += 1
                    merged = True
                    break

            if not merged:
                break 
# Hurdle 
green = 0 
yellow = 0 
x = {}
y = {}
def solve():
    for i in range(3): 
        for j in range(3): 
            if guess[i][j] == answer[i][j]: 
                green += 1
            else: 
                x[guess[i][j]] = x.get(guess[i][j], 0) + 1
                y[answer[i][j]] = y.get(answer[i][j], 0) + 1

    for i, x_count in x.items(): 
        if i in y: 
            if x_count < y[i]: 
                yellow += x_count 
            else: 
                yellow += y[i]
    return yellow, green
# Lonely_photo
def solve():
    import sys
    input = sys.stdin.readline
    
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
    x = len(arr)
    y = 1 
    result = 0
    while x >= 3: 
        z = arr
        for j in range(y):
            NumG = 0 
            NumH = 0 
            for i in range(x): 
                if z[i] == "G":
                    NumG += 1 
                if z[i] == "H": 
                    NumH += 1 
            if NumG == 1 or NumH == 1: 
                result += 1
            z = z[1:]
        x -= 1
        y += 1
    return result 