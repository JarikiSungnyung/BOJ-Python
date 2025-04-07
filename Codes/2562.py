num = 0
where = 0

for i in range(9):
    N = int(input())
    if N > num:
        num = N
        where = i + 1

print(num)
print(where)