T = int(input())

for i in range(T):
    result = ""
    R, S = input().split()
    R = int(R)
    for j in range(len(S)):
        result += S[j] * R
    print(result)