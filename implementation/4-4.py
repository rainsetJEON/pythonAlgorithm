# 4-4 게임 개발

n , m = map(int, input().split())

 # 맵 초기화
#d = [[0]*m for _ in range(n)]

d = []
for _ in range(n):
    d.append([0]*m)

print(d)