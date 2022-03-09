# 백준 괄호

import sys


def sol(num):

    # n = int((input()))

    for i in range(num):
        input_data = input()
        arr = []

        for j in input_data:
            if j == "(":
                arr.append(j)
            elif j == ")":
                if len(arr) != 0 and arr[-1] == "(":
                    arr.pop()
            else:
                arr.append(")")
                break
    if len(arr) == 0:
        print('YES')
    else:
        print('NO')


    pass


if __name__ == '__main__':
    with open('Parenthesis String.txt') as f:
        sys.stdin = f
        input = sys.stdin.readline

        n = int((input()))

        result = sol(n)