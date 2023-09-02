'''
# 자료구조의 기초 (data structure)

1. stack
선입후출의 구조(FILO)
후입선출의 구조(LIFO)

'''

# 5-1. 스택예제
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)
stack.append(6)

# print(stack[::-1])  # 최상단 원소부터 출력
# print(stack)

'''
2. Queue
선입선출의 구조(FIFO)
'''

# 5-2. 큐 예제
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  # 먼저 들어온 5 삭제
queue.pop()   # 나중에 들어온 7 삭제

queue.append(4)
queue.reverse()

# print(queue)

# print(list(queue))  # 큐를 리스트 자료형으로 변환

'''
3. 재귀함수 (recursive function)

# 5-3. 재귀함수 예제

def recursive_function():
    print('재귀함수를 호출합니다.')
    recursive_function()

recursive_function()

==> 이렇게 하게 되면 무한으로 자기 자신을 호출해서 오류 발생
==> 따라서 재귀함수의 종료조건을 반드시 명시해야 함
'''

# 5-4, 재귀 함수 종료 예제
def recursive_function(i):
    # 20번 출력했을 때 종료되도록 종료 조건 명시
    if i == 20:
        return
    
    print(i,'번쨰 재귀함수에서', i+1,'번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

# recursive_function(1)


# 5-5. 2가지 방식으로 구현한 팩토리얼 예제
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1,n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <=1:
        return 1
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력 (n=5)
# print('반복적으로 구현:', factorial_iterative(5))
# print('재귀적으로 구현:', factorial_recursive(5))


'''
 # 탐색 알고리즘 DFS/BFS
 
 1. DFS (depth-first-search) / 깊이 우선 탐색
 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

  - 그래프의 기본 구조
  노드(node,정점(vertex)), 간선(edge)
 
  - 그래프 2가지 방식
  인접 행렬(Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현하는 방식
   인접행렬 방식은 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
   2차원 리스트로 구현 가능
   연결되어 있지 않은 노드끼리는 '무한(의 비용)'이라고 작성
   
  인접 리스트(Adjacency List): 리스트로 그래프의 연결 관계를 표현하는 방식
   모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
   '연결 리스트' 자료 구조 이용 (C++이나 자바는 연결리스트 표준 라이브러리를 제공)
   파이썬은 기본 자료형인 리스트의 append() 메소드 이용, 2차원 리스트로 구현 가능

 '''

# 5-6. 인접 행렬 방식 예제
INF = 99999 # 무한의 비용 선언
 
 # 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

# print(graph)

# 5-7. 인접 리스트 방식 예제
 # 행(row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

 # 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

 # 노드 1에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append({0,7})

 # 노드 2에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0,5))

# print(graph)

'''
# 두 방식의 차이점
메모리와 속도 측면에서 살펴보자.
* 메모리 측면
인접 행렬 방식 : 모든 관계를 저장, 노드 개수가 많을수록 메모리가 불필요하게 낭비
인접 리스트 방식 : 연결된 정보만을 저장, 메모리 효율적으로 사용 가능
* 속도 측면
인접 리스트 방식은 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다.

# DFS의 스택 자료 구조를 이용한 동작 과정
 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
'''

# 5-8. DFS 예제
 # DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end= ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

 # 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

 # 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

 # 정의된 DFS 함수 호출
# dfs(graph, 1, visited)


'''
2. BFS (breath first search) / 너비 우선 탐색
가까운 노드부터 탐색하는 알고리즘 (DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식)
보통 선입선출 방식인 큐 자료구조를 이용

# BFS의 큐 자료구조를 이용한 동작 과정
 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
'''

# 5-9. BFS 예제
from collections import deque

 # BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 적용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end= ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

 # 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

 # 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

 # 정의된 BFS 함수 호출
bfs(graph, 1, visited)

