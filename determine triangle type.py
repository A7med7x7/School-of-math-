x1 =int(input("enter x1 : "))
y1 =int(input("enter y1 : "))
x2 =int(input("enter x2 : "))
y2 =int(input("enter y2 : "))
x3 =int(input("enter x3 : "))
y3 =int(input("enter y3 : "))
#طلبنا من المستخدم ادخال بيانات المثلثات(الاحداثيات ) x and y 
x = (x1 + y1)
y = (x2 + y2)
z = (x3 + y3)
#جمعنا الاحداثيات 
a = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
#المعادلة لتكوين المثلث
if (a == 0):
    print ("collinear")
#اذا كان الناتج = الصفر 
else:
    print ("Not colinear")
#اذا الناتج ما بيساوي الصفر
if x == y == z:
    print("Equilateral ")
#اذا تساوت الثلاثة احداثيات بينتج مثلث متساوي الاضلاع
elif x == y or y == z or z == x:
    print("Isosceles ")
#اذا تساوت احد الاضلاغ بينتج مثلث متساوي الساقين
else:
    print("Scalene ")
#ما دون ذلك ينتج مثلث مختلف الاضلاع
