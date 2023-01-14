while True:
    N = int(input("N : "))
    
    if (N > 100000):
        print("range N : 1 <= N <= 100,000, try again")
    else:
        break
    
dir = list(input("direction: ").split())
dirList = list(map(int,dir))


count1 = 0
count2 = 0


for i in dirList:
    if dirList[i] == dirList[i+1] and dirList[i] == 1:
        count1 += 1
    elif dirList[i] == dirList [i-1] == 1 and dirList[i] != dirList[i+1]:
        count1 += 1
    elif dirList[i] == dirList[i+1] and dirList[i] == 2:
        count2 += 1
    elif dirList[i] == dirList[i-1] == 2 and dirList[i] != dirList[i+1]:
        count2 += 1
    else:
        pass


result = count1 - count2
print(result)


