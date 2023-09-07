# p.197 부품찾기
'''
동빈이네 전자 매장에는 n개의 제품이 있다.
제품은 모두 정수 형태의 고유한 번호가 있다.
손님이 m개의 제품을 대량 구매해 부품 m개에 대한 종류를 모두 파악해야 한다.
가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
'''

# 7-5.py 답안 예시 (이진 탐색)
 # 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # mid > target ; 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # mid < target ; 오른쪽 확인
        else:
            start = mid + 1
    return None

 # n 제품 개수 입력
n = int(input())
 # 가게에 있는 전체 제품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort()  # 이진 탐색을 수행하기 위해 사전에 배열 정렬
 # m 손님이 주문한 제품 개수 입력
m = int(input())
 # 손님이 주문한 제품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

 # 손님이 확인 요청한 제품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')



# 7-6.py 답안 예시 (계수 정렬)
 # n 입력
n = int(input())
array = [0] * 1000001

 # 가게에 있는 전체 제품 번호를 입력 받아서 기록
for i in input().split():
    array[int(i)] = 1

 # m 입력
m = int(input())

 # 손님이 요청한 제품 번호 입력
x = list(map(int, input().split()))
 # 손님이 요청한 제품 번호 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')



# 7-7.py 답안 예시 (집합 자료형 이용)
n = int(input())

 # 가게에 있는 전체 부품 번호를 입력받아서 집합자료형에 기록
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

