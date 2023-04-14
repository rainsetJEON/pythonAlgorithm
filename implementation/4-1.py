# 4-1 상하좌우


n = int(input())

plan = list(input().split())

x, y = 1, 1

for i in plan:
    if i == "U" and x!=1:
        x -= 1
    elif i == "D" and x != n:
        x += 1
    elif i == "R" and y != n:
        y += 1
    elif i == "L" and y != 1:
        y -= 1

print(x,y)


'''
# 예시 답안
dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for i in plan:
    for s in range(len(move_types)):
        if i == plan[s]:
            nx = x + dx[s]
            ny = y + dy[s]
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue
x, y = nx, ny
print(x, y)

'''


