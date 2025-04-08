T = int(input())
check = 0

for i in range(T):
    H, W, N = map(int, input().split())
    for j in range(1, W + 1):
        for k in range(1, H + 1):
            check += 1
            if check == N:
                print(f"{k*100+j}")
                check = 0
                break
        if check == 0:
            break