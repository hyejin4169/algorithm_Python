# 백준 다리 놓기

import sys


def factorial(n):

    f = 1
    for i in range(n):
        f *= (i+1)
    return f

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    print(factorial(m) // (factorial(n) * factorial(m-n)))

    pass


if __name__ == '__main__':
    with open('bridge.txt') as f:
        sys.stdin = f
        input = sys.stdin.readline

        n = int(input())

        result = factorial(n)