# 3-2 큰 수의 법칙

# N 배열 크기, M 더해지는 횟수, K 반복가능횟수
n , m, k = map(int, input().split())  # N,M,K 공백으로 구분하여 입력받기
data = list(map(int, input().split())) # N개의 수를 공백으로 구분하여 입력받기


data.sort()
first = data[n-1]
second = data[n-2]

'''
# 내 답안
count = m // k
count2 = m % k

result = first*k*count + second*count2


print(result)
'''

# 정답 답안

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)
