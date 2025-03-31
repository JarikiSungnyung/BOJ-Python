isLeap = False

year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            isLeap = True
        else:
            isLeap = False
    else:
        isLeap = True
else:
    isLeap = False
    
print(1 if isLeap else 0)