# 백준 설탕 배달

import sys


def sol(num):

    count = 0
    # 수를 세기 위한 count 변수

    while num >= 0:
    # 총 무게가 0kg보다 크거나 같을때까지 반복
        if num % 5 == 0:
        # 5로 나눠 0이 되면
            count += int(num // 5)
            # count에 5를 나눈 숫자를 더해줌
            print(count)
            break

        num -= 3
        count += 1
    # 나누어 떨어지지 않으면 num(총 무게)에 3을 빼고 count에 1을 더함

    else:
        print(-1)
    # 0으로 나누어 떨어지지 않을 시 -1 출력

    pass


if __name__ == '__main__':

    with open('sugarDelivery.txt') as f:
        sys.stdin = f
        input = sys.stdin.readline

        n = int(input())

        result = sol(n)