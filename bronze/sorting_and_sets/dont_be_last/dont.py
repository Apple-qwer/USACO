def solve(): 
    import sys
    input = sys.stdin.readline 
    N = int(input())
    total = { } 
    for _ in range(N): 
        name, value = input().split()
        value = int(value)
        total[name] = total.get(name, 0) + value  
    
    x = set() 
    for i in total.values():
        x.add(i) 
    
    sorted_list = sorted(x)

    for name, value in total.items( ): 
        if value == sorted_list[1]: 
            print(name)
    
if __name__ == "__main__": 
    solve()

    


    


