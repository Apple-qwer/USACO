# Astral_superpostion
import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N, A, B = map(int, input().split())
        grid = [input().strip() for _ in range(N)]

        init = [[0]*N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 'B':
                    init[r][c] = 1
                    pr, pc = r - B, c - A
                    if pr < 0 or pc < 0:
                        print(-1)
                        break
                    init[pr][pc] = 1
            else:
                continue
            break
        else:

            bad = False
            for r in range(N):
                for c in range(N):
                    if grid[r][c] == 'W':
                        if init[r][c]:
                            bad = True
                        pr, pc = r - B, c - A
                        if 0 <= pr < N and 0 <= pc < N and init[pr][pc]:
                            bad = True
            if bad:
                print(-1)
                continue

        
            for r in range(N):
                for c in range(N):
                    if grid[r][c] == 'G':
                        pr, pc = r - B, c - A
                        if 0 <= pr < N and 0 <= pc < N and init[pr][pc]:
                            has_prev = True
                        else:
                            has_prev = False
                        if not has_prev and not init[r][c]:
                            init[r][c] = 1

            total = 0
            for r in range(N):
                for c in range(N):
                    if init[r][c] == 1:
                        total += 1
            print(total)
            continue

        continue

if __name__ == "__main__":
    solve()

# Roundabout_Round

def solve():
    import sys
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        N = int(input())
        answer = 0

        length = 2

        while True:
            start = ""
            for i in range(length - 1):
                start += "4"
            start += "5"
            start = int(start)

            end = "4"
            for i in range(length - 1):
                end += "9"
            end = int(end)

            if start > N:
                break

            if end > N:
                answer += N - start + 1
            else:
                answer += end - start + 1

            length += 1

        print(answer)

#Acrobat
N, M, K = map(int, input().split())
 
cows = []
for _ in range(N):
	w, a = map(int, input().split()) #w = weight of the cow, a = how manys cows that have that weight 
	cows += [w] * a #make list of everysingle cows 
cows.sort(reverse=True) #reverse the list 
 
answer = 0 #count how many towers are established 
for _ in range(M): #every iteration to make one tower 
	remaining_cows = [] # cows that hasn't been placed this iteration 
	current_cow = 1e100 #arbitrary large number/weight of the last cow 
	for cow in cows: #iterate through the cow list 
		if cow + K <= current_cow: #ensures that weight gap between the cows are large enough 
			current_cow = cow # update the last placed cow to keep track 
			answer += 1 # answer increase as a cow become part of a tower 
		else:
			remaining_cows += [cow] # no more cows can fit into this tower so save it for next iteration 
 
	if len(remaining_cows) == 0: # no more cows left so we break out of the loop 
		break
	cows = remaining_cows # so that we update the list for the next iteration so we don't count any cows repetively 
 
print(answer) # print answer after the iteration 


if __name__ == "__main__":
    solve()
