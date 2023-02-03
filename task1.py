# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = input()
summa = 0
for i in num:
    summa += int(i)
print(summa)