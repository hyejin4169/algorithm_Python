# 백준 스택

import sys


def sol(num):

    stack = []

    for i in range(n) :

        word = sys.stdin.readline().split()
        order = word[0]

    #order가 push 인 경우
    if order == 'push':
        value = word[1]
        stack.append(value)

    # order가 pop 인 경우
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    # order가 size 인 경우
    elif order == 'size':
        print(len(stack))

    # order가 empty 인 경우
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # order가 top 인 경우
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    pass


if __name__ == '__main__':
    with open('stack.txt') as f:
        sys.stdin = f
        input = sys.stdin.readline

        n = int(input())

        result = sol(n)