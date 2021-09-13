input_1 = int(input("Введите количество билетов - "))
age = [int(input("Введите возраст - ")) for i in range(input_1)]
Summa = []
for each in age:
    if each < 18:
        a = 0
    elif 18 <= each < 25:
            a = 990
    else:
        a = 1390
    Summa.append(a)
print ("Цена билетов без скидки - ", (sum(Summa)), "рублей")
a = sum(Summa)
if input_1 > 3:
    a = (a - a * 10 // 100)
print ("Цена билетов со скидкой - ", a, "рублей")