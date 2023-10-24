# 멀리뛰기 lv2
# 피보나치 수열 
# 1,1,2,3,5,8,13,21,,,

#DP 이용 => dynamic programming, 동적 프로그래밍

# 코드1 그냥 푼거
def solution(n):
    answer = 0
    
    # 피보나치 수열! : 1,1,2,3,5,8,13,21,,,
    
    # 피보나치
    if n== 1:
        answer = 1
    elif n== 2:
        answer =2
    else:
        a,b = 1,2
        for i in range(n-2):
            a,b = b, a+b
    
    answer = b
    return answer

def DP(n):
    dp = dict()
    # 지금은 딕셔너리로 선언했지만
    # dp = [] *(n+1) 로 해도 됨
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    answer = dp[n]

    return answer
