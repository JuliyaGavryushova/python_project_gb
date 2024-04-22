"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"


def sum_frac(f1, f2):
    num1 = f1.split("/")
    num2 = f2.split("/")
    sum_znam = int(num1[1]) * int(num2[1])
    sum_chis = sum_znam // int(num1[1]) * int(num1[0]) + sum_znam // int(num2[1]) * int(num2[0])
    res1 = str(sum_chis) + "/" + str(sum_znam)
    return res1


def prov_frac(f1, f2):
    num1 = f1.split("/")
    num2 = f2.split("/")
    prov_znam = int(num1[1]) * int(num2[1])
    prov_chis = int(num1[0]) * int(num2[0])
    res2 = str(prov_chis) + "/" + str(prov_znam)
    return res2


result1 = sum_frac(frac1, frac2)
result2 = prov_frac(frac1, frac2)

print("Сумма дробей:", result1)
print("Произведение дробей:", result2)
print("Сумма дробей (для проверки):", Fraction(frac1) + Fraction(frac2))
print("Произведение дробей (для проверки):", Fraction(frac1) * Fraction(frac2))