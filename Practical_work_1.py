money = int(input("Введите сумму: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposite_1 = int(money*per_cent['ТКБ'] / 100)
deposite_2 = int(money*per_cent['СКБ'] / 100)
deposite_3 = int(money*per_cent['ВТБ'] / 100)
deposite_4 = int(money*per_cent['СБЕР'] / 100)
deposit = []
deposit.append(deposite_1)
deposit.append(deposite_2)
deposit.append(deposite_3)
deposit.append(deposite_4)
print("Накопленные средства за год вклада в каждом из банков:", deposit)
print("Максимальная сумма, которую Вы можете заработать:", max(deposit))
