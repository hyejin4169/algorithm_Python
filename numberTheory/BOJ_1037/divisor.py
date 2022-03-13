# 백준 약수

import sys


def sol(num):

    # N = int(input())
    A = list(map(int, input().split()))

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