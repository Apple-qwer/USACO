
from itertools import combinations # to use itertools combinations 
#I decided to loop through everything after seeing that 1<= K <= 10 and 1 <= N <= 20
def solve(): 
    import sys 
    input = sys.stdin.readline 
    K, N = map(int,input().split()) 
    practices = [] 
    for i in range(K): # making nested list of results of the practices 
        o = list(map(int, input().split()))
        practices.append(o)
    possible_pairs = 0 
    for cow1, cow2 in combinations(range(1, N + 1), 2): #using combinations to first set up pairs 
        cow1_win = 0 # these cow_wins is the tract if there is a consistency in skill difference 
        cow2_win = 0 # if one has 0 at the end of the loop means either one of the cow gets better scores than them all the time meaning they can form a pair 
        for i in range(K): #iterating through all the practices 
            cow1_pos = 0 #cow_pos is to determine the positions of the cow to see who did better
            cow2_pos = 0 
            for j in range(N): #iterating through all the cows to find the index of the paired cows 
                if cow1 == practices[i][j]: 
                    cow1_pos = j 
                if cow2 == practices[i][j]: 
                    cow2_pos = j 
            if cow1_pos < cow2_pos:  #after iterating use the cow_pos to see who did better and mark who did better
                cow1_win += 1 
            else: 
                cow2_win += 1
        
        if cow1_win == 0 or cow2_win == 0: # if one of them is equal to zero that suggests that one of the cow always did better than the other
            possible_pairs += 1 # so they become a pair and I add 1 to possible pair 
    
    print(possible_pairs)#print all the possible pairs after iterations. 

if __name__ == "__MAIN__": 
    solve()
        
                    





            


