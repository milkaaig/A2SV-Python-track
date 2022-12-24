n=int(input())
dic ={}
for  i in range(n):
    word =input()
    if word in dic:
        dic[word]+=1
    else :
        dic[word]=1
print(len(dic))
for key in dic:
    print(dic[key], end=" ")
