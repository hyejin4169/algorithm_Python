# 백준 다리 놓기

import sys
import math

sys.stdin = open("bridge.txt","r")

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)

    pass


# if __name__ == '__main__':
#     with open('bridge.txt','r') as f:
#         sys.stdin = f
#         input = sys.stdin.readline
#
#         n = int(input())
#
#         result = factorial(n)