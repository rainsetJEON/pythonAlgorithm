# 3-4 1이 될 때까지

n, k = map(int, input().split())

count = 0

while n!=1:
    if n % k ==0:
        n = n/k
        count +=1
    else:
        n -= 1
        count +=1


print(count)


'''
# 예시 답안
result = 0

 # n이 k 이상이라면 k로 계속 나누기
while n >= k:
    while n % k != 0 :
        n -= 1
        result += 1
    n //= k
    result += 1
 # 마지막으로 남은 수에 대하여 1씩 빼기
while n>1:
    n -=1
    result +=1

print(result)

'''

