tc = int(input())

for i in range(tc):
    a, b = list(map(int, input().split()))
    
    print(min(min(a,b), (a + b) //4))
