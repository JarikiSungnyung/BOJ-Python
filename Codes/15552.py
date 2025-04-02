import sys

T = int(sys.stdin.readline().rstrip())

for i in range (T):
    N, M = map(int, sys.stdin.readline().split())
    print(N + M)