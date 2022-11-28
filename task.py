# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму
vvodnoe2 = input("Число для второй задачи: ")


def fill(a):
    if a == 1:
        return 1
    else:
        return a * fill(a - 1)


def nabor(elem):
    result = []
    for i in range(1, elem):
        result.append(fill(i))
    print(result)
