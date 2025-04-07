def circulate(a, b):
    return (a+b) * (a-b)

A, B = map(int, input().split())
print(circulate(A, B))