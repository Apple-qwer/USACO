# Blocks
from itertools import permutations

def solve():
    import sys
    input = sys.stdin.readline


    n = int(input())


    dices = [input().strip() for _ in range(4)]

    words = [input().strip() for _ in range(n)]

    for word in words:
        possible = False
        length = len(word)

        
        for dice_order in permutations(range(4), length):
            match = True 
            for i in range(length):
                letter = word[i]
                dice_index = dice_order[i]
                if letter not in dices[dice_index]:
                    match = False
                    break  
            if match:
                possible = True
                break 
        if possible:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()

# Walking_home
def solve():
    import sys
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input().strip())
        K = int(input.strip())
        grid = []
        for i in range(N):
            grid.append(input().strip())
       

        total_paths = 0
        stack = []
        if N > 1 and grid[0][1] != 'H':
            stack.append((0, 1, "R", 0))
        if N > 1 and grid[1][0] != 'H':
            stack.append((1, 0, "D", 0))

        while stack:
            r, c, direction, turns = stack.pop()
            if r == N - 1 and c == N - 1:
                total_paths += 1
                continue

            if turns > K:
                continue
            if c + 1 < N and grid[r][c + 1] != 'H':
                if direction == "R":
                    stack.append((r, c + 1, "R", turns))
                else:
                    stack.append((r, c + 1, "R", turns + 1))
            if r + 1 < N and grid[r + 1][c] != 'H':
                if direction == "D":
                    stack.append((r + 1, c, "D", turns))
                else:
                    stack.append((r + 1, c, "D", turns + 1))

        print(total_paths)

if __name__ == "__main__":
    solve()

# Drought ?