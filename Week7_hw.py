# Feeding the cows
def solve(): 
    import sys 
    input = sys.stdin.readline 
    n = int(input())
    for i in range(n): 
        N, K = map(int, input().strip().split())
        cows = input().strip()
        patch_idx = ["." for _ in range(N)]
        if K == 0: 
            print(len(cows))
            print(cows)
            continue
        patch_count = 0 
        G = True 
        H = True 
        G_cover = 0
        H_cover = 0
        for i in range(len(cows)): 
            if i <= N - 1:
                if cows[i] == "G" and G: 
                    if i + K <= N - 1: 
                        patch_idx[i + K] = "G"
                    elif patch_idx[N - 1] == "." or patch_idx[N - 1] == "G": 
                        patch_idx[N - 1] = "G"
                    else: 
                        patch_idx[N - 2] = "G"
                    patch_count += 1
                    G_cover = i + K + K
                    G = False 
                elif cows[i] == "H" and H:
                    if i + K <= N - 1: 
                        patch_idx[i + K] = "H"
                    elif patch_idx[N - 1] == "." or patch_idx[N - 1] == "H": 
                        patch_idx[N - 1] = "H"
                    else: 
                        patch_idx[N - 2] = "H"
                    patch_count += 1
                    H_cover = i + K + K
                    H = False 
                if G_cover == i: 
                    G = True 
                if H_cover == i: 
                    H = True 
            else: 
                if cows[N - 1] == "G" and G: 
                    patch_idx[N - 1] = cows[N - 1]
                    patch_count += 1
                elif cows[N - 1] == H and H:
                    patch_idx[N - 1] = cows[N - 1]
                    patch_count += 1
        print(patch_count)
        for i in range(len(patch_idx)):
            if i < len(patch_idx) - 1:
                print(patch_idx[i], end = (""))
            else: 
                print(patch_idx[i])
if __name__ == "__main__": 
    solve()

# Stamp Grid
# Solution
def solve():
    import sys
    input = sys.stdin.readline
    
    T = int(input())
    def rotate(mat): 
        K = len(mat)
        x = [["."] * K for _ in range(K)]
        for i in range(K): 
            for j in range(K):
                x[i][j] = mat[K - 1 - j][i]
        return x 
                
    
    for _ in range(T):
        N = int(input())

        target = [list(input().strip()) for _ in range(N)]


        K = int(input())

        stamp = [list(input().strip()) for _ in range(K)]

        rot0 = stamp
        rot1 = rotate(rot0)
        rot2 = rotate(rot1)
        rot3 = rotate(rot2)
        rotations = [rot0, rot1, rot2, rot3]

        can = [[False] * N for i in range(N)]
        for rot in rotations: 
            for i in range(N - K + 1): 
                for j in range(N - K + 1): 
                    safe = True 
                    for a in range(K): 
                        for b in range(K): 
                            if rot[a][b] == "*" and target[i + a][j + b] == ".": 
                                safe = False 
                                break 
                        if not safe:
                            break
                    if not safe: 
                        continue 
                    for a in range(K):
                        for b in range(K):
                            if rot[a][b] == '*':
                                can[i + a][j + b] = True
                            
        possible = True 
        for i in range(N): 
            for j in range(N): 
                if target[i][j] == "*" and not can[i][j]: 
                    possible = False 
                    break
            if not possible: 
                break 

        if possible: 
            print("YES")
        else: 
            print("NO")
if __name__ == "__main__": 
    solve()




