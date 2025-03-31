input = input()
num = input.split()
num1 = int(num[0])
num2 = int(num[1])
if num1 > num2:
    print(">")
elif num1 < num2:
    print("<")
else:
    print("==")