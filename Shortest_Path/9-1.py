# 최단 경로 (shortes path)
'''
길 찾기 문제

* 종류
 - 다익스트라 최단 경로 알고리즘
 - 플로이드 워셜
 - 밸만 포드 알고리즘
이 중 우리는 다익스트라와 플로이드 워셜을 다뤄보자

최단 경로 유형은 그리디 알고리즘 및 다이나믹 프로그래밍 알고리즘과 한 유형으로 볼 수 있다.
'''

# 1. 다익스트라 최단 경로 알고리즘
# Dijkstra 알고리즘이란?
'''
그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
'음의 간선'이 없을 때 정상적으로 동작한다.
 # 음의 간선 : 0보다 작은 값을 가지는 간선

* 동작 원리
1. 출발 노드 선택
2. 출발 노드로부터 다른 노드로 가는 비용 계산
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택

=> 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것
'''

# 방법1. 간단한 다익스트라 알고리즘
'''
시간 복잡도 : O(V^2) : V = 노드의 개수
단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)
'''

# tip) 모든 리스트는 (노드의 개수 + 1)의 크기로 할당하여, 노드의 번호를 인덱스로 하여 바로 리스트에 접근할 수 있도록 한다.
# 그래프를 표현해야 할 때 많이 사용하는 방법!


# 9-1.py 간단한 다익스트라 알고리즘 소스코드
 # 입력되는 데이터의 수가 많으므로 파이썬 내장함수 sys.std.readline() 사용
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

 # 노드의 개수, 간선의 개수 입력
n,m = map(int(input().split()))
 # 시작 노드 번호 입력
start = int(input())
 # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
 # 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
 # 최단 거리 테이블은 모두 무한으로 초기화
distance = [INF] * (n+1)

 # 모든 간선 정보 입력
for _ in range(m):
    a,b,c = map(int(input().split()))   # a에서 b로 가는 비용이 c라는 의미
    graph[a].append((b,c))

 # 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0   # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstar(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

 # 다익스트라 알고리즘 수행
dijkstar(start)

 # 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INF) 출력
    if distance[i] == INF:
        print('infinity')
    # 도달할 수 있는 경우, 거리를 출력
    else:
        print(distance[i])
