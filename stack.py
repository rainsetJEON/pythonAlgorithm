# 프로그래머스 스택 예제
# 문제 이름 : 올바른 괄호 ; (,)의 짝 맞는지 확인하기 
def solution(s):
    tmp = []
    for x in s:
        tmp.append(x)
        if len(tmp) > 1 and tmp[-1] == tmp[-2]:
            tmp.pop()
            tmp.pop()

    if len(tmp) == 0:
        return 1
    else:
        return 0