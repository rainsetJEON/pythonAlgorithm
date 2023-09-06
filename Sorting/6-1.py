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
시간 복잡도 : O(N^2) / BUT 거의 정렬되어 있는 상태라면 O(N)까지 나오며, 퀵 정렬보다 빠름
'''

# 6-3.py 삽입 정렬 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):   # range(start, end, step) : start인덱스부터 end+1 인덱스까지 step만큼 변화
        if array[j] < array[j-1]:  # 한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

# print(array)

# continue, pass, break의 차이점
# continue : 다음 루프 수행, 반복을 유지한 상태에서 코드의 실행만 건너뜀
# pass : 영향 x
# break : 반복문을 멈추고 루프 밖으로 나감, for와 while 문법에서 벗어남



# 3. 퀵 정렬
'''
가장 많이 사용되는 알고리즘, 빠른 정렬 알고리즘! 
=> 기준을 정한 후 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식 (기준 : 피벗(pivot))
=> 피벗을 설정하고 리스트를 분할하는 다양한 방법이 있음, 여기서는 '호어 분할(Hoare Partition) 방식'을 다뤄보자.
시간 복잡도 : O(NlogN) 단, 최악의 경우 O(N^2) (이미 데이터가 정렬되어 있는 경우)
'''

# 6-4.py 퀵 정렬 소스코드
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:   # 원소가 1개인 경우 종료
        return
    
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1)
    quick_sort(array, right +1, end)

quick_sort(array, 0, len(array) -1)
# print(array)



# 6-5.py 파이썬의 장점을 살린 퀵 정렬 소스코드
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort2(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <=1 :
        return array
    
    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

# print(quick_sort2(array))



# 4. 계수 정렬 (count sort) 
'''
특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
 => 조건 : 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 (가장 작은 데이터와 큰 데이터의 차이 < 1,000,000 일 때 효과적)
데이터의 개수 N, 최댓값 K일 때, 최악의 경우의 시간 복잡도 : O(N + K)

특징 : 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다.
* [방법]
초기 : 7 5 9 0 3 1 6 2 9 1 4 8 0 5 2
1. 가장 작은 데이터 = 0, 가장 큰 데이터 = 9 파악하기
2. 데이터의 범위가 0~ 9 이므로 크기가 10인 리스트 선언 (처음에는 리스트의 모든 데이터를 0으로 초기화)
3. 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가
4. 각 인덱스의 값은 데이터의 개수를 의미하는 것이므로, 인덱스 * 인덱스의 값 만큼 출력
'''

# 6-6.py 계수 정렬 소스코드
'''
 # 모든 원소의 값이 0이상으로 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
 # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1   # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):   # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')   # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
'''


# 6-7.py 파이썬의 기본 정렬 라이브러리 sorted(), sort()
array = [7,5,9,0,3,1,6,2,4,8]

result1 = sorted(array)
print(result1)

array.sort()
print(array)


# 6-9.py 정렬 라이브러리에서 key를 활용한 소스코드
'''
sorted() 혹은 sort()를 이용할 때 key 매개변수를 입력으로 받을 수 있다.
key 값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 된다.
ex) 리스트의 데이터가 튜플로 구성되어 있을 때, 각 데이터의 두 번째 원소를 기준으로 설정하는 경우 예시와 같은 소스코드를 작성할 수 있다.
 혹은 람다 함수를 사용할 수 있다. 
'''

array = [('banana', 2), ('apple', 5), ('carrot', 3)]

def setting(data):
    return data[1]

result = sorted(array, key = setting)
print(result)



