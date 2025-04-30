remainder = list()

for i in range(10):
    n = int(input())
    remainder.append(n % 42)

remainder = set(remainder)
print(len(remainder))