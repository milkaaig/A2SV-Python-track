# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
b = []
ga , gb = list(map(int, input().split()))
 
for i in range(1,ga+1):
    val = input()
    d[val].append(i)
for i in range(1,gb+1):
    b.append(input())
for i in b:
    if i in d:
      print(*d[i])
    else:
        print(-1)
    
