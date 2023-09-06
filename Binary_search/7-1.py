# 이진 탐색
# 탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘

# 1. 순차 탐색 (sequential search)
# 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
'''
보통, 정렬되지 않은 리스트에서 사용
리스트 안에 특정 값의 원소가 있는지 체크할 때 or 특정 값의 개수를 count() 할 때에도 사용
'''


# 7-1.py 순차 탐색 소스코드

def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i+1   # 현재의 위치(인덱스) 반환
'''        
 # n, target 입력
input_data = input().split()
n = int(input_data[0]) 
target = input_data[1]

 # array 입력
array = input().split()

 # 순차 탐색 결과 출력
# print(sequential_search(n,target,array))
'''



# 2. 이진 탐색 (binary search)
'''
내부의 데이터가 정렬되어 있을 때만 사용 가능!
탐색 범위를 절반씩 좁혀가며 데이터를 탐색
 ㄴ>범위가 절반씩 줄어든다는 점에서 퀵 정렬과 공통점, 이진 탐색은 원소의 개수도 절반으로 줄어드는 점이 차이점
변수 3개 : 시작점, 끝점, 중간점
시간 복잡도 : O(logN)
'''

# 7-2.py 재귀 함수로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2  # 중간점 설정
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # mid > target ; 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # mid < target ; 오른쪽 확인 
    else:
        return binary_search(array, target, mid+1, end)

 # n과 target 입력
n, target = list(map(int, input().split()))
 # array 입력
array = list(map(int, input().split()))

 # 이진 탐색 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print('None')
else:
    print(result + 1)


