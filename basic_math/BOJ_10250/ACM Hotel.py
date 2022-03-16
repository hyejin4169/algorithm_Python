# 백준 ACM 호텔

import sys


def sol(num):
    for i in range(num):
        H, W, N = map(int, input().split())
        # H: 각 호텔의 층 수, W: 각 층의 방 수, N: 몇 번째 손님
        floor = N % H
        # 몇 번째 손님을 호텔 층수로 나눈 나머지 값을 floor(층수)에 담는다
        room = N // H + 1
        # 나눈 몫에 +1을 해서 room(방 번호)에 담는다
        if floor == 0:
            # 입력받는 N이 호텔 층수를 나타내는 H의 배수인 경우
            room -= 1
            # room에 -1을 해서 저장
            floor = H
            # floor에 H값을 저장

        print(floor * 100 + room)

    pass


if __name__ == '__main__':
    with open('ACM Hotel.txt') as f:
        sys.stdin = f
        input = sys.stdin.readline

        n = int(input())

        result = sol(n)