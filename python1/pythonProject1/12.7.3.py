per_cent ={'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму - "))
deposit_1 = money * per_cent['ТКБ'] / 100
deposit_2 = money * per_cent['СКБ'] / 100
deposit_3 = money * per_cent['ВТБ'] / 100
deposit_4 = money * per_cent['СБЕР'] / 100
deposit = []
deposit.append(deposit_1)
deposit.append(deposit_2)
deposit.append(deposit_3)
deposit.append(deposit_4)
print(deposit)

print('Максимальная сумма, которую вы можите заработать - ', max(deposit))