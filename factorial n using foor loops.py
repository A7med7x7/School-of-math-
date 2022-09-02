#cs homework factorial n using for loops
x = 1
n = int(input("what is your number: "))
for i in range(1,n+1):
    x = x * i

print("factorial of your number is",n,"is",x)