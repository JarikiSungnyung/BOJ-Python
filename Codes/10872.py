N = int(input())

M = 1
k = 1

for i in range(N):
    M *= k
    k += 1

print(M)