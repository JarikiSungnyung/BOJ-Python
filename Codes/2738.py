N, M = map(int, input().split())

matrix1 = list()
matrix2 = list()
result = list()

for i in range(N):
    row1 = list(map(int, input().split()))
    matrix1.append(row1)

for i in range(N):
    row2 = list(map(int, input().split()))
    matrix2.append(row2)

for i in range(N):
    row_sum = list()
    for j in range(M):
        row_sum.append(matrix1[i][j] + matrix2[i][j])
    result.append(row_sum)

for row in result:
    print(" ".join(map(str, row)))
