# p.182 두 배열의 원소 교체
'''
동빈이는 두 개의 배열 A,B를 가지고 있다. 두 배열은 N개의 원소로 구성
A와 B에서 최대 K번의 바꿔치기 연산 가능, 최종 목표는 A의 모든 원소의 합이 최대가 되도록 하는 것
'''

# 풀이 공략
'''
A의 최소값들과 B의 최대값들을 교체, 단, A의 최소값이 B의 최대값보다 작을 때에만 교체 수행
'''

# 답안 예시

n,k = map(int, input().split())   # n,k 입력 받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()   # 배열 A는 오름차순 정렬
b.sort(reverse=True)   # 배열 B는 내림차순 정렬

 # 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else:  # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))   # 배열 A의 모든 원소의 합 출력