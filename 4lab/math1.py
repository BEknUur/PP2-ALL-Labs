#1
# Write a Python program to convert degree to radian.
import math
b=int(input())
c=math.radians(b)
print(c)

#2
#Write a Python program to calculate the area of a trapezoid.
def area(height, base_first, base_second):
    total_area = (base_first + base_second) / 2 * height
    return total_area

height = int(input())
base_first = int(input())
base_second = int(input())

result = area(height, base_first, base_second)
print(result)

#3
#Write a Python program to calculate the area of regular polygon.
import math

def polygon(side, length):
    area = (side * length ** 2)/(4 * math.tan(math.pi / side))
    return area

side = int(input())
length = int(input())

result = polygon(side,length)
print(result)



#4
#Write a Python program to calculate the area of a parallelogram
def parallelogram(length,height):
    c=length*height
    return c

length=float(input())
height=float(input())
sol=parallelogram(length,height)
print(sol)


