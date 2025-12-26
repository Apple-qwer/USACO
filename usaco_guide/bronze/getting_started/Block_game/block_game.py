import sys 
import string # found on google 
def solve(): 
    input = sys.stdin.readline 
    N = int(input())
    alphabet_dict = {i: 0 for i in string.ascii_lowercase} #im creating a dictionary of alphabet to keep track of how much each alphabet appears 
    for _ in range(N):  # looping to figure out the amount of blocks required for each line 
        front, back = map(str, input().split())
        for i in front: 
            alphabet_dict[i] += 1
        for i in back: 
            alphabet_dict[i] += 1
    
    for i in string.ascii_lowercase: #after loop just print the values in a-z order which is just first to last 
        print(alphabet_dict[i])

if __name__ == "__MAIN__": 
    solve()




    
