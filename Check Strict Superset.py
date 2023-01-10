A = set(input().split())
N = int(input())
boolval = True
for i in range(N):
    Nset = ()
    Nset = set(input().split())
    if A.difference(Nset) != 0 and Nset.difference(A):
        boolval = False
print(boolval) 
