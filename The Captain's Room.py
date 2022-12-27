# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
sizeofgroup = int(input())
rmlst = list(input().split())
# length = len (rmlst)
# rmdic = {}
# for i in range(length):
#     rm = rmlst[i]
#     if rm in rmdic:
#         rmdic[rm] += 1
#     else:
#         rmdic[rm] = 1
# # print(rmdic)
# for rm in rmdic:
#     if rmdic[rm] != sizeofgroup:
#         print(rm)
#         break
rmdic = Counter(rmlst)
key_of_min_value = min(rmdic, key=rmdic.get)
print(key_of_min_value)
