# the random function generates a random fractional number between 0 and 1
from random import random
print("A programm for calculate the sum of digits of a random 3-digit number:")
#when multiplied by 900, you get a random number between 9 and 899. (9) If you add 100, you get a number between 100 and 999. (9)
n = random() * 900 + 100

#I discard the fractional part, the number is displayed
n = int (n)
print(n)

#The first digit (most significant bit) of the number is extracted by dividing it by 100
a = n // 100

#Division by 10 removes the last digit of the number. Then finding the remainder when dividing by 10 extracts the last digit that was the middle in the original number
b = (n // 10) % 10

#The last digit (least significant bit) of a number is found by finding the remainder when divided by 10.
c = n % 10

#The sum of the digits is calculated and displayed
print("The calculated sum of the digits will be as follows:")
print(a + b + c)
print ("Thank you for using this program!")