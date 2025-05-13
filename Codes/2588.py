A = int(input())
Bin = input()
B = list()

for i in range(len(Bin)):
    B.append(int(Bin[2-i]))
    print(A*B[i])

print(A*int(Bin))