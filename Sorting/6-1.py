# 정렬 sorting

'''
정렬 ; 데이터를 특정한 기준에 따라서 순서대로 나열 
 # 정렬 종류
 - 선택 정렬
 - 삽입 정렬
 - 퀵 정렬
 - 계수 정렬

tip : 기본적으로 오름차순 정렬을 하자 / 내림차순은 reverse() 사용하자
'''

# 1. 선택 정렬
'''
가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정 반복
시간 복잡도 : O(N^2)  -> 이중 반복문을 사용하기 때문

다른 알고리즘과 비교했을 때, 비효율적!! BUT 특정한 리스트에서 가장 작은 데이터를 찾는 일이 코딩테스트에서 많이 출제됨
 => 선택 정렬 사용
'''
# 6-1.py 선택 정렬 소스코드

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프

# print(array)

 # 6-2.py 파이썬 스와프(swap) 소스코드
# 0 인덱스와 1 인덱스의 원소 교체
array = [3,5]
array[0], array[1] = array[1], array[0]

# print(array)


# 2. 삽입 정렬
'''
데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하면 어떨까?
특징 : 두 번째 데이터부터 시작 (첫 번째 데이터는 그 자체로 정렬되어 있다고 판단함)
'''

# 6-3.py 삽입 정렬 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):   # range(start, end, step) : start인덱스부터 end+1 인덱스까지 step만큼 변화
        if array[j] < array[j-1]:  # 한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)

# continue, pass, break의 차이점
# continue : 다음 루프 수행, 반복을 유지한 상태에서 코드의 실행만 건너뜀
# pass : 영향 x
# break : 반복문을 멈추고 루프 밖으로 나감, for와 while 문법에서 벗어남


