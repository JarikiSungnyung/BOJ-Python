n = int(input())
for i in range(n):
    result = 0
    count = 1
    str = input()
    for j in range(len(str)):
        if str[j] == 'O':
            result += count
            count += 1
        else:
            count = 1

    print(result)
    