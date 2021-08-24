#Импортируется модуль math, содержащий различные математические функции
import math

#функция input() возвращает строку
print ("Данная программа позволяет найти площадь и периметр прямоугольного треугольника.")
AB = input ("Введите длину первого катета: ")
AD = input ("Введите длину второго катета: ")

#строки переводятся в вещественыне числа
AB = float(AB)
AD = float(AD)

#Находим гипотенузу по теореме Пифагора: "сумма квадратов катетов равна квадрату гипотенузы" Функция sqrt() из модуля math извлекает квадратный корень.Оператор ** возводит в квадрат.
BC = math.sqrt(AB ** 2 + AD ** 2)

#Площадь прямоугольного треугольника равна половине площади соответсвующего прямоугольника.
S = (AB * AD) / 2

#Периметр находится как сумма всех сторон.
P = AB + AD + BC

print ("Площадь треугольника: %.2f" % S)
print ("Периметр треугольника: %.2f" % P)