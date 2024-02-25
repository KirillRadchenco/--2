a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
sum = 0

for i in range(a+1):
    if i % b == 0:
        sum += i

print("Сумма всех чисел от 0 до", a, "делящихся на", b, "без остатка равна", sum)
