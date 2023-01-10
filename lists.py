if __name__ == '__main__':
    N = int(input())
    thelist = []
    for j in range(N):
        command = list(input().split())
        if command[0] == "insert":
            i = int(command[1])
            e = int(command[2])
            thelist.insert(i,e)
        elif command[0] == "print":
            print(thelist)
        elif command[0] == "remove":
            e = int(command[1])
            thelist.remove(e)
        elif command[0] == "append":
            e = int(command[1])
            thelist.append(e)
        elif command[0] == "sort":
            thelist.sort()
        elif command[0] == "pop":
            thelist.pop()
        elif command[0] == "reverse":
            thelist.reverse()
            
           
