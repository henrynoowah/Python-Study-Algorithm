# 설탕 배달 / 수학 / 다이나믹 프로그래밍 / 그리디 알고리즘
# https://www.acmicpc.net/problem/2839

# ---------문제해석-----------------------------------------------------------------------
'''
N kg의 설탕을 3kg, 5kg 두 종류의 봉지로 나누어 담아간다.
필요한 봉지의 최솟값을 구한다.
'''

# ---------접근방법---------------------------------------------------------------------- 
'''
N을 5로 나눈 나머지가 3으로 나누어 떨어지는지 구한다.
나머지가 1,2,3,4 일 때 3kg 봉지의 갯수를 구한다. 
'''

# ----------------------------------------------------------------------------------------
import sys

def solution(N):
    answer = 0
    if (N % 5) % 3 == 0:    # 나머지 3
        answer += (N // 5) + (N % 5) // 3

    elif ((N % 5) + 5) % 3 == 0 and ((N % 5) + 5) < N:    # 나머지 1, 4 ---> 1+5=6 / 4+5=9 ---> 3으로 나누어 떨어짐 and +5 한 나머지가 N보다 작아야 함 (4, 7)
        answer += ((N // 5) -1) + (((N % 5) + 5) // 3)

    elif ((N % 5) + 10) % 3 == 0 and ((N % 5) + 10) < N:   # 나머지 2
        answer += ((N // 5) -2) + (((N % 5) + 10) // 3)

    elif N % 3 == 0:    # 5kg 봉지를 쓸 수 없으면, 3kg 봉지만으로 가능한지 
        answer += N // 3

    else:
        answer = -1

    print(answer)


input = int(sys.stdin.readline())

solution(input)


# ----------------------------------------------------------------------------------------
'''
메모리 
29200 KB

시간
72 ms

코드길이
538 B
'''




