print("Введите первое число:")
a = float(input())
print("Введите второе число:")
b = float(input())

sum = a + b # сумма
dif = a - b # разность
com = a * b # произведение

print(str(a) + " + " + str(b) + " = " + str(sum))
print(str(a) + " - " + str(b) + " = " + str(dif))
print(str(a) + " * " + str(b) + " = " + str(com))
if b != 0:
    pri = a / b  # частное
    print(str(a) + " : " + str(b) + " = " + str(pri))
