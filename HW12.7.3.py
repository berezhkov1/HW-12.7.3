per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада в рублях: '))
deposit = []
if money < 1000:
    print('Ошибка. Минимальная сумма вклада - 1 000 рублей')
else:
    deposit.append(int(per_cent['ТКБ']*money))
    deposit.append(int(per_cent['СКБ']*money))
    deposit.append(int(per_cent['ВТБ']*money))
    deposit.append(int(per_cent['СБЕР']*money))
    print(deposit)
    print('Максимальная сумма, которую вы можете заработать —', max(deposit), 'рублей')
