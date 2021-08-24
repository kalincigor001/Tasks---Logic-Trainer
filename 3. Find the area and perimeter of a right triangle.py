#Imported math module containing various math functions
import math

#the input () function returns a string
print ("This program allows you to find the area and perimeter of a right-angled triangle.")
AB = input ("Enter the length of the first leg: ")
AD = input ("Enter the length of the second leg: ")

#strings are converted to real numbers
AB = float(AB)
AD = float(AD)

#Find the hypotenuse according to the Pythagorean theorem: "the sum of the squares of the legs is equal to the square of the hypotenuse" The sqrt () function from the math module extracts the square root. The ** operator squares.
BC = math.sqrt(AB ** 2 + AD ** 2)

#The area of a right-angled triangle is half the area of the corresponding rectangle.
S = (AB * AD) / 2

#The perimeter is found as the sum of all sides.
P = AB + AD + BC

print ("The area of the triangle is: %.2f" % S)
print ("The perimeter of the triangle is: %.2f" % P)
print ("Thank you for using this program!")