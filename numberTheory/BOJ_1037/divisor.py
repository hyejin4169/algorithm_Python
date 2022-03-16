# 백준 약수

import sys


def sol(num):

    # N = int(input())
    # input은 입력된 값을 문자열로 인식
    # 입력된 값을 숫자로 인식하기 위해 int 함수 이용(정수로 변환)
    A = list(map(int, input().split()))
    # 입력값을 두 개 이상으로 구분하기 위해 split함수 사용
    # input().split()를 사용하여 각각의 값을 리스트로 나누어줌
    # int 함수는 리스트는 정수형으로 바꾸어줄 수 없기 때문에 map함수 이용(모든 자료형 각각에 함수 적용 가능)

    max_num = max(A)
    min_num = min(A)

    # 가장 큰 값과 작은 값을 곱하면 N을 구할 수 있음

    print(max_num * min_num)

    pass


if __name__ == '__main__':
    with open('divisor.txt') as f:
        sys.stdin = f
        input = sys.stdin.readline

        N = int(input())

        result = sol(N)