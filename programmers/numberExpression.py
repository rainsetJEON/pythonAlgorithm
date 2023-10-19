def solution(n):
    result = 1
    for i in range(1, n//2+1):
        sum = 0
        while sum<n:
            sum = sum+i
            
            if sum == n:
                result +=1
                break
            i +=1
    return result

# 여기서 배울 수 있는 점
# 이중 for문 사용 대신 for문 + while 문을 통해 시간효율성을 높일 수 있다.

# 나의 원래 답안
def solution(n):
    result = 1
    for i in range(1, (n//2)+1):
        sum = i
        for j in range(i+1, (n//2)+2):
            
            sum = sum+j
            if sum == n:
                result +=1
                break
    return result