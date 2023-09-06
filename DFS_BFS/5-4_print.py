# p.152 미로 탈출

'''
N x M 크기의 직사각형 형태의 미로
현재 위치 (1,1), 출구(N,M), 벽 0, 길 1
탈출하기 위해 움직여야하는 최소 칸의 개수를 구하시오.
(단, 시작 칸(왼쪽 위)과 마지막 칸(오른쪽 아래) 포함해서 계산)
'''

# BFS를 활용
# 이유 : BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문

from collections import deque

 # N,M을 공백으로 구분하여 입력 받기
n,m = map(int, input().split())

 # 2차원 리스트의 앱 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

 # 이동할 네 방향 정의(상,하,좌,우)
dx = [-1, 1, 0, 0]  #세로
dy = [0, 0, -1, 1]  #가로

 # BFS 코드 구현
def bfs(x,y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))

    print(queue)
    # 큐가 빌 때까지 반복
    while queue:
        x,y = queue.popleft()

        print('x=', x, 'y=', y)
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print('nx=',nx, 'ny=',ny)
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                print('graph = ', graph)
                queue.append((nx, ny))

                print('queue=',queue)
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

 # BFS 수행한 결과 출력
print(bfs(0,0))