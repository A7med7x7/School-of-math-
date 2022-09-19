x = 0
y = 0
x1 = int(input("what is your first x: "))
y1 = int(input("what is your first y: "))
x2 = int(input("what is your second x: "))
y2 = int(input("what is your second y: "))
x3 = int(input("what is your third x: "))
y3 = int(input("what is your third y: "))
x4 = int(input("what is your fourth x: "))
y4 = int(input("what is your fourth y: "))

distance1 = abs((x1 - x)**2 + (y1 - y)**2)**0.5
distance2 = abs((x2 - x)**2 + (y2 - y)**2)**0.5
distance3 = abs((x3 - x)**2 + (y3 - y)**2)**0.5
distance4 = abs((x4 - x)**2 + (y4 - y)**2)**0.5
print(distance2)

my_list = [distance1, distance2,distance3,distance4]
my_list.sort()
print(my_list)

"""if distance1 < distance2 and distance3 and distance4:
    print(distance1, "distance1 is the nearest to the origin")
elif distance2 < distance1 and distance3 and distance4:
        print(distance2, "distance2 is the nearest")
elif distance3 < distance1 and distance2 and distance4:
        print(distance3, " distance3 is the nearest")
elif distance4 < distance1 and distance2 and distance3:
        print(distance4, "distance4 is the nearest")"""



"""s0 = 0
s1 = (x1 + y1)
s2 = (x2 + y2)
s3 = (x3 + y3)
s4 = (x4 + y4)

if s1 < s2 and s4 and s4:
    print(s1, "is the nearest to the origin")
elif s2 < s1 and s3 and s4:
    print(s2, "is the nearest")
elif s3 < s1 and s2 and s4:
    print(s3, "is the nearest")
elif s4 < s1 and s2 and s3:
    print(s4, "is the nearest")
"""