# Enter your code here. Read input from STDIN. Print output to STDOUT
test = int(input())
for i in range(test):
    lenb = int(input())
    blocks = list(map(int, input().split()))
    vc = [float('inf')]
    right = len(blocks) - 1
    left = 0
    while left <= right:
        if blocks[left] < blocks[right]:
            if blocks[right] > vc[-1]:
                print("No")
                break
            else:
                vc.append(blocks[right])
                right -= 1
                
        elif blocks[left] > blocks[right]:
            if blocks[left] > vc[-1]:
                print("No")
                break
            else:
                vc.append(blocks[left])
                left +=1
        else:
            if blocks[left] > vc[-1]:
                print("No")
                break
            else:
                print("Yes")
                break
            
                
