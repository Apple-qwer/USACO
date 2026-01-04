def solve(): 
    from collections import deque #using deque to appendleft and popleft 
    import sys 

    input = sys.stdin.readline 
    N, M = map(int,input().split())
    speed_limit = [] 
    cow_speed = []
    for _ in range(N): #making a list for the speed_limits 
        x, y = map(int,input().split()) 
        speed_limit.append([x, y])
    for _ in range(M): #making a list for bessie's driving speeds
        x, y = map(int,input().split()) 
        cow_speed.append([x,y])
    speed_limit = deque(speed_limit) 
    cow_speed = deque(cow_speed)
    over_limit = 0 
    while cow_speed and speed_limit: #runnning until both of them runs out so after the car travels 100miles 
        cow_d, cow_s = cow_speed.popleft() 
        d, s = speed_limit.popleft()
        if d != cow_d: # if distance does not equal the cow distance that means one of the distance will be an excess so I'm managing that 
            if d > cow_d: 
                d = d - cow_d # substracting the dinstance and appending it back into the list 
                speed_limit.appendleft([d, s])
            elif cow_d > d: 
                cow_d = cow_d - d #same thing 
                cow_speed.appendleft([cow_d, cow_s])
        
        if s < cow_s: #this means bessie has exceeded the speed limit 
            over_limit = max(over_limit, cow_s - s) #updating the value of over_limit if its lower doesn't update, if its bigger it updates 
    print(over_limit)      # after loop all the speeding has been managed so print out over_limit

if __name__ == "__main__": 
    solve()
    
        




