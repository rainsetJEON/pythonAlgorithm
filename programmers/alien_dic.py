def solution(spell, dic):
    answer = 2
    sum = 0
    n = len(spell)
    m = len(dic)
    
    for j in range(0,m):
        sum = 0
        for i in range(0,n):
            print(i)
            if spell[i] in dic[j]:
                print("1 if")
                sum += 1
                if sum == n:
                    print("2 if")
                    answer = 1
                else:
                    continue
            else:
                continue
                    
        
    return answer
        
        