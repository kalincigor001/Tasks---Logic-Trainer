# функция random генерирует
# случайное дробное число от 0 до 1
from random import random

#при умножении на 900 получается 
#случайное число от 9 до 899.(9)
#Если прибавить 100, то получится
#число от 100 до 999.(9)
n = random() * 900 + 100

#Отбрасывается дробная часть,
#число выводится на экран
n = int (n)
print(n)

#Извлекается первая цифра
#(старший разряд) числа путем
#деления нацело на 100
a = n // 100

#Деление нацело на 10 удаляет
#последнюю цифру числа.
#Затем нахождение остатка
#при делении на 10 извлекает
#последнюю цифру, которая в 
#исходном числе была средней
b = (n // 10) % 10

#Последняя цифра (младший разряд)
#числа находится путем нахождения
#остатка при делении нацело на 10.
c = n % 10

#Вычисляется сумма цифр и выводится на экран
print(a + b + c)