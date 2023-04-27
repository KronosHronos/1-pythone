ticket_number = input("Введите номер билета: ")

# Проверяем, является ли номер шестизначным
if len(ticket_number) != 6:
    print("Некорректный номер билета")
else:
    # Вычисляем сумму первых трех цифр и сумму последних трех цифр
    sum_first = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    sum_last = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
    
    # Проверяем, является ли билет счастливым
    if sum_first == sum_last:
        print("Счастливый билет!")
    else:
        print("Обычный билет :(")