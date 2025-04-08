A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
mul = list(str(mul))

for i in range(len(mul)):
    mul[i] = int(mul[i])
    
for i in range(10):
    print(mul.count(i))