num1 = int(input("what is your first number?"))
num2 = int(input("what is your second number?"))
num3 = int(input("what is your third number?"))

if num1 > num3 and num2:
    print("the number",num1,"is the greatest")
elif num2 > num3 and num1:
    print("the number", num2,"is the greater")
elif num3 > num2 and num1:
    print("number",num3,"is the greatest")
else:
    print("they are all equal")
