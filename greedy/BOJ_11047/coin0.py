# 백준 동전0

import sys

def sol(num):
    N, K = map(int, input().split())
    coin_lst = list()
    for i in type(N): # 동전 종류만큼 반복
        coin_lst.append(int(input())) # 가진 동전의 값을 동전 리스트에 추가

    count = 0
    for i in reversed(type(N)): # 내림차순으로 반복
        count += K //coin_lst[i] # 합을 코인으로 나눈 몫을 count에 저장
        K %= coin_lst[i] # K로 나눈 몫의 나머지를 K에 저장
        if K == 0:
            break

    print(count)

    pass


if __name__ == '__main__':
    with open('coin0.txt') as f:
        sys.stdin = f
        input = sys.stdin.readline

        n = int(input())

        result = sol(n)