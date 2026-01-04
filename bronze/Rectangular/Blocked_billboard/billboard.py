import sys
input = sys.stdin.readline

def solve():
    rects = []
    for _ in range(3):                    
        rects.append(list(map(int, input().split())))

    ans = 0
    for i in range(2):                    
        x1, y1, x2, y2 = rects[i]
        tx1, ty1, tx2, ty2 = rects[2]

        area = (x2 - x1) * (y2 - y1)

        w = min(x2, tx2) - max(x1, tx1) #find the overlapping length 
        h = min(y2, ty2) - max(y1, ty1) #find the overlapping height 
        if w < 0: 
            w = 0
        if h < 0: 
            h = 0

        ans += area - w * h

    print(ans)

solve()
