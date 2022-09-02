num1 = int(input("what is your first number?"))
num2 = int(input("what is your second number?"))
num3 = int(input("what is your third number?"))

if num1 > num3 and num2:
    print(num1)
elif num2 > num3 and num1:
    print(num2)
else:
    if num3 > num2 and num1:
        print (num3)