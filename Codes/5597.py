N = list(i for i in range(1, 31))

for i in range(0, 28):
    A = int(input())
    N.remove(A)

print("\n".join(map(str, N)))
