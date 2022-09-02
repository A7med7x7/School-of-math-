x1 =int(input("enter x1 : "))
y1 =int(input("enter y1 : "))
x2 =int(input("enter x2 : "))
y2 =int(input("enter y2 : "))
x3 =int(input("enter x3 : "))
y3 =int(input("enter y3 : "))

x = (x1 + y1)
y = (x2 + y2)
z = (x3 + y3)

a = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

if (a == 0):
    print ("collinear")
else:
    print ("Not colinear")

if x == y == z:
    print("Equilateral ")

elif x == y or y == z or z == x:
    print("Isosceles ")

else:
    print("Scalene ")