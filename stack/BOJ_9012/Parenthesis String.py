# 백준 괄호

import sys


def sol(num):

    # n = int((input()))

    for i in range(n):
        stack = []
        a = input()
        for j in a:
            if j == '(':
                stack.append(j)
                # '(' 괄호가 들어오면 stack에 넣어줌
            elif j == ')':
                if stack:
                    stack.pop() # ')' 괄호가 들어왔을 때 stack이 비어있지 않다면 pop해줌
                else:  # 스택이 비어있다면
                    print("NO") #NO 출력
                    break
        else:  # break가 난 적 없다면 else문 실행
            if not stack:  # 스택이 비어있다면 괄호의 짝이 모두 맞으므로
                print("YES") #YES 출력
            else:  # else문 실행해도 스택에 괄호가 들어있다면 짝이 맞지 않으므로
                print("NO") #NO 출력

    pass


if __name__ == '__main__':
    with open('Parenthesis String.txt') as f:
        sys.stdin = f
        input = sys.stdin.readline

        n = int((input()))

        result = sol(n)