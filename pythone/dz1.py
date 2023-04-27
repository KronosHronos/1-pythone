number = int(input("Введите трехзначное число: "))

# Разделяем цифры числа и складываем их
digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10
sum_of_digits = digit1 + digit2 + digit3

print("Сумма цифр введенного числа равна:", sum_of_digits)