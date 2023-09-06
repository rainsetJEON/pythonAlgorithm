# 4-4 게임 개발
# p121

n , m = map(int, input().split())

 # 1-1. 맵 초기화 -> 리스트 내포(list comprehension)
d = [[0]*m for _ in range(n)]

 # 풀어쓰면 다음과 같음!
'''
d = []
for _ in range(n):
    d.append([0]*m)

'''

 # 1-2. 현재 캐릭터의 x,y좌표 및 방향을 입력받기
x,y,direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리


 # 2. 전체 맵 정보 입력받기
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


 # 3.북, 동, 남, 서 방향
dy = [0, +1, 0, -1]
dx = [-1, 0, +1, 0]


 # 4. 왼쪽으로 회전
def turn_left():
    global direction
    direction -=1
    if direction == -1:
        direction = 3


 # 4. 시물레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and arr[nx][ny] ==0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4 :
        nx = x - dx[direction]
        


