# importing constant pi from math module
from math import pi 
print("A program for calculating the length of the year on a particular planet.")
r = input("Indicate the radius of the planet's orbit (million km): ")
v = input("Indicate the orbital speed of the planet (km / s): ")

#I translate the string into real numbers
r = float(r)
v = float (v)

#I translate millions of kilometers into just kilometers
r = r * 1000000

#The year, expressed in seconds, is the circumference (2 * Pi * R) i.e. orbits, and is divided by the speed
year = 2 * pi * r / v

#to convert seconds to days, divide by 60 to get minutes, then divide by 60 to get hours, then divide by 24 to get days
year = year / (60 * 60 * 24)
yearText = ("Here are how many days one year lasts on this planet:")
print (yearText, round(year))
print ("Thank you for using this program!")