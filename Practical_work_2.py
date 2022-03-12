tickets = int(input("Введите количество билетов: "))
price = 0
for i in range(tickets):
    i += 1
    guest_age = int(input("Введите возраст посетителя: "))
    if guest_age < 18:
        print("Цена билета: 0 руб.")
    elif 18 <= guest_age < 25:
        price += 990
        print("Цена билета: 990 руб.")
    else:
        price += 1390
        print("Цена билета: 1390 руб.")
if tickets >= 3:
    price = price - (price * 0.1)
    print(f"Сумма к оплате с учетом скидки: {price} руб.")
else:
    print(f"Сумма к оплате: {price} руб.")
